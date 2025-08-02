#!/usr/bin/env python3
"""
Development Agent for TMNT API
Interactive CLI for managing the local development environment
"""
import os
import sys
import subprocess
import signal
import time
import json
import threading
import queue
from pathlib import Path
from datetime import datetime
import argparse
import psutil

try:
    from rich.console import Console
    from rich.table import Table
    from rich.live import Live
    from rich.layout import Layout
    from rich.panel import Panel
    from rich.syntax import Syntax
    from rich import print as rprint
except ImportError:
    print("Installing required packages...")
    subprocess.run([sys.executable, "-m", "pip", "install", "rich", "psutil"])
    from rich.console import Console
    from rich.table import Table
    from rich.live import Live
    from rich.layout import Layout
    from rich.panel import Panel
    from rich.syntax import Syntax
    from rich import print as rprint

console = Console()

class DevAgent:
    def __init__(self):
        self.server_process = None
        self.log_queue = queue.Queue()
        self.monitoring = False
        self.pid_file = Path(".dev-agent.pid")
        
    def start_server(self, background=False):
        """Start the development server"""
        if self.is_running():
            console.print("[yellow]Server is already running![/yellow]")
            return
        
        console.print("[green]Starting TMNT API server...[/green]")
        
        if background:
            # Start in background mode
            self.server_process = subprocess.Popen(
                [sys.executable, "run_local.py"],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1,
                preexec_fn=os.setsid if os.name != 'nt' else None
            )
            # Save PID
            with open(self.pid_file, 'w') as f:
                f.write(str(self.server_process.pid))
            
            console.print(f"[green]✓ Server started in background (PID: {self.server_process.pid})[/green]")
            console.print("[cyan]Run 'python dev-agent.py logs' to view logs[/cyan]")
        else:
            # Run in foreground
            try:
                subprocess.run([sys.executable, "run_local.py"])
            except KeyboardInterrupt:
                console.print("\n[yellow]Server stopped[/yellow]")
    
    def stop_server(self):
        """Stop the development server"""
        if not self.is_running():
            console.print("[yellow]Server is not running[/yellow]")
            return
        
        console.print("[yellow]Stopping server...[/yellow]")
        
        # Try to get PID from file
        if self.pid_file.exists():
            try:
                with open(self.pid_file) as f:
                    pid = int(f.read().strip())
                
                # Kill the process group
                if os.name != 'nt':
                    os.killpg(os.getpgid(pid), signal.SIGTERM)
                else:
                    subprocess.run(["taskkill", "/F", "/PID", str(pid)])
                
                # Clean up PID file
                self.pid_file.unlink()
                console.print("[green]✓ Server stopped[/green]")
            except Exception as e:
                console.print(f"[red]Error stopping server: {e}[/red]")
        else:
            # Try to find and kill uvicorn processes
            for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
                try:
                    if 'uvicorn' in proc.info['name'] or \
                       (proc.info['cmdline'] and 'api.index:app' in ' '.join(proc.info['cmdline'])):
                        proc.terminate()
                        console.print(f"[green]✓ Stopped process {proc.info['pid']}[/green]")
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass
    
    def restart_server(self):
        """Restart the development server"""
        console.print("[yellow]Restarting server...[/yellow]")
        self.stop_server()
        time.sleep(1)
        self.start_server(background=True)
    
    def is_running(self):
        """Check if server is running"""
        if self.pid_file.exists():
            try:
                with open(self.pid_file) as f:
                    pid = int(f.read().strip())
                # Check if process exists
                psutil.Process(pid)
                return True
            except (psutil.NoSuchProcess, ValueError):
                # Clean up stale PID file
                self.pid_file.unlink()
        return False
    
    def show_status(self):
        """Show server status and system info"""
        table = Table(title="Development Environment Status")
        table.add_column("Component", style="cyan")
        table.add_column("Status", style="green")
        table.add_column("Details")
        
        # Server status
        if self.is_running():
            with open(self.pid_file) as f:
                pid = int(f.read().strip())
            server_status = "[green]Running[/green]"
            server_details = f"PID: {pid}"
        else:
            server_status = "[red]Stopped[/red]"
            server_details = "Not running"
        
        table.add_row("API Server", server_status, server_details)
        
        # Python version
        python_version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
        table.add_row("Python", f"[green]{python_version}[/green]", sys.executable)
        
        # Check .env file
        env_exists = Path(".env").exists()
        env_status = "[green]Found[/green]" if env_exists else "[yellow]Missing[/yellow]"
        table.add_row("Environment", env_status, ".env file")
        
        # Check Convex connection
        try:
            from api.convex_client import convex_client
            convex_status = "[green]Connected[/green]" if convex_client._connected else "[yellow]Fallback[/yellow]"
        except:
            convex_status = "[red]Error[/red]"
        table.add_row("Convex DB", convex_status, "Database connection")
        
        # Port availability
        port_free = not self._is_port_in_use(8000)
        port_status = "[yellow]In use[/yellow]" if not port_free and not self.is_running() else "[green]Available[/green]"
        table.add_row("Port 8000", port_status, "API port")
        
        console.print(table)
        
        # Show URLs if running
        if self.is_running():
            console.print("\n[cyan]Available endpoints:[/cyan]")
            console.print("  • API Docs: http://localhost:8000/docs")
            console.print("  • API Root: http://localhost:8000/api")
            console.print("  • Health:   http://localhost:8000/api/health")
    
    def _is_port_in_use(self, port):
        """Check if a port is in use"""
        import socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            return s.connect_ex(('localhost', port)) == 0
    
    def tail_logs(self, follow=True, lines=50):
        """Tail server logs"""
        if not self.is_running():
            console.print("[yellow]Server is not running[/yellow]")
            return
        
        console.print(f"[cyan]Showing last {lines} log lines...[/cyan]")
        console.print("[dim]Press Ctrl+C to stop[/dim]\n")
        
        # For now, suggest using the foreground mode for logs
        console.print("[yellow]Note: Real-time log tailing works best when running server in foreground mode[/yellow]")
        console.print("[cyan]Run 'python dev-agent.py start' (without --background) for live logs[/cyan]")
    
    def reset_database(self):
        """Reset the Convex database"""
        console.print("[yellow]Resetting database...[/yellow]")
        
        with console.status("Clearing database..."):
            result = subprocess.run([sys.executable, "scripts/clear_convex.py"], capture_output=True, text=True)
            if result.returncode == 0:
                console.print("[green]✓ Database cleared[/green]")
            else:
                console.print(f"[red]✗ Error clearing database: {result.stderr}[/red]")
                return
        
        with console.status("Populating database..."):
            result = subprocess.run([sys.executable, "scripts/populate_convex.py"], capture_output=True, text=True)
            if result.returncode == 0:
                console.print("[green]✓ Database populated[/green]")
            else:
                console.print(f"[red]✗ Error populating database: {result.stderr}[/red]")
    
    def run_tests(self, pattern=None):
        """Run tests"""
        console.print("[cyan]Running tests...[/cyan]")
        
        cmd = ["pytest", "-v"]
        if pattern:
            cmd.extend(["-k", pattern])
        
        subprocess.run(cmd)
    
    def check_endpoints(self):
        """Check API endpoints"""
        if not self.is_running():
            console.print("[yellow]Server is not running. Start it first.[/yellow]")
            return
        
        console.print("[cyan]Checking API endpoints...[/cyan]")
        
        try:
            import httpx
        except ImportError:
            console.print("[yellow]Installing httpx...[/yellow]")
            subprocess.run([sys.executable, "-m", "pip", "install", "httpx"])
            import httpx
        
        endpoints = [
            ("API Root", "http://localhost:8000/api"),
            ("Health", "http://localhost:8000/api/health"),
            ("Turtles", "http://localhost:8000/api/v1/turtles"),
            ("Villains", "http://localhost:8000/api/v1/villains"),
            ("Episodes", "http://localhost:8000/api/v1/episodes"),
        ]
        
        table = Table(title="API Endpoint Status")
        table.add_column("Endpoint", style="cyan")
        table.add_column("Status")
        table.add_column("Response Time")
        
        with httpx.Client() as client:
            for name, url in endpoints:
                try:
                    start = time.time()
                    response = client.get(url, timeout=5.0)
                    elapsed = (time.time() - start) * 1000
                    
                    if response.status_code == 200:
                        status = f"[green]✓ {response.status_code}[/green]"
                    else:
                        status = f"[yellow]⚠ {response.status_code}[/yellow]"
                    
                    table.add_row(name, status, f"{elapsed:.0f}ms")
                except Exception as e:
                    table.add_row(name, f"[red]✗ Error[/red]", str(e))
        
        console.print(table)

    def open_browser(self):
        """Open the homepage in the default browser"""
        if not self.is_running():
            console.print("[yellow]Server is not running. Starting it first...[/yellow]")
            self.start_server(background=True)
            time.sleep(2)
        
        import webbrowser
        url = "http://localhost:8000"
        console.print(f"[cyan]Opening {url} in your browser...[/cyan]")
        webbrowser.open(url)

def main():
    parser = argparse.ArgumentParser(description="TMNT API Development Agent")
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # Start command
    start_parser = subparsers.add_parser('start', help='Start the development server')
    start_parser.add_argument('--background', '-b', action='store_true', help='Run in background')
    
    # Other commands
    subparsers.add_parser('stop', help='Stop the development server')
    subparsers.add_parser('restart', help='Restart the development server')
    subparsers.add_parser('status', help='Show server status')
    subparsers.add_parser('logs', help='Show server logs')
    subparsers.add_parser('reset-db', help='Reset the database')
    subparsers.add_parser('check', help='Check API endpoints')
    subparsers.add_parser('open', help='Open homepage in browser')
    
    # Test command
    test_parser = subparsers.add_parser('test', help='Run tests')
    test_parser.add_argument('pattern', nargs='?', help='Test pattern to match')
    
    args = parser.parse_args()
    
    if not args.command:
        console.print("[cyan]TMNT API Development Agent[/cyan]")
        console.print("\nAvailable commands:")
        console.print("  start [--background]  Start the development server")
        console.print("  stop                  Stop the development server")
        console.print("  restart               Restart the development server")
        console.print("  status                Show server status")
        console.print("  logs                  Show server logs")
        console.print("  reset-db              Reset the database")
        console.print("  check                 Check API endpoints")
        console.print("  open                  Open homepage in browser")
        console.print("  test [pattern]        Run tests")
        console.print("\nExample: python dev-agent.py start --background")
        return
    
    agent = DevAgent()
    
    if args.command == 'start':
        agent.start_server(background=args.background)
    elif args.command == 'stop':
        agent.stop_server()
    elif args.command == 'restart':
        agent.restart_server()
    elif args.command == 'status':
        agent.show_status()
    elif args.command == 'logs':
        agent.tail_logs()
    elif args.command == 'reset-db':
        agent.reset_database()
    elif args.command == 'check':
        agent.check_endpoints()
    elif args.command == 'open':
        agent.open_browser()
    elif args.command == 'test':
        agent.run_tests(args.pattern)

if __name__ == "__main__":
    main()