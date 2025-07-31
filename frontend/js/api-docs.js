// API Documentation Interactive Features

// Tab switching functionality
function showTab(tabName) {
    // Hide all tab contents
    const tabContents = document.querySelectorAll('.tab-content');
    tabContents.forEach(tab => {
        tab.classList.remove('active');
    });
    
    // Remove active class from all tab buttons
    const tabButtons = document.querySelectorAll('.tab-btn');
    tabButtons.forEach(btn => {
        btn.classList.remove('active');
    });
    
    // Show selected tab
    const selectedTab = document.getElementById(tabName);
    if (selectedTab) {
        selectedTab.classList.add('active');
    }
    
    // Add active class to clicked button
    const activeButton = document.querySelector(`[onclick="showTab('${tabName}')"]`);
    if (activeButton) {
        activeButton.classList.add('active');
    }
}

// Copy code functionality
function copyCode(button) {
    const codeBlock = button.closest('.code-block');
    const code = codeBlock.querySelector('code').textContent;
    
    navigator.clipboard.writeText(code).then(() => {
        // Change button text to indicate success
        const originalText = button.textContent;
        button.textContent = 'Copied!';
        button.classList.add('copied');
        
        // Reset button after 2 seconds
        setTimeout(() => {
            button.textContent = originalText;
            button.classList.remove('copied');
        }, 2000);
    }).catch(err => {
        console.error('Failed to copy:', err);
        button.textContent = 'Failed';
        setTimeout(() => {
            button.textContent = 'Copy';
        }, 2000);
    });
}

// Smooth scrolling for sidebar navigation
document.addEventListener('DOMContentLoaded', () => {
    // Add smooth scrolling to all sidebar links
    const sidebarLinks = document.querySelectorAll('.api-nav a[href^="#"]');
    
    sidebarLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const targetId = link.getAttribute('href');
            const targetSection = document.querySelector(targetId);
            
            if (targetSection) {
                const headerOffset = 100;
                const elementPosition = targetSection.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.pageYOffset - headerOffset;
                
                window.scrollTo({
                    top: offsetPosition,
                    behavior: 'smooth'
                });
                
                // Update active link styling
                sidebarLinks.forEach(l => l.classList.remove('active'));
                link.classList.add('active');
            }
        });
    });
    
    // Highlight current section in sidebar while scrolling
    const sections = document.querySelectorAll('.api-section, .endpoint-group');
    const navLinks = document.querySelectorAll('.api-nav a');
    
    const highlightNavigation = () => {
        let scrollPosition = window.scrollY + 150;
        
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.offsetHeight;
            const sectionId = section.getAttribute('id');
            
            if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
                navLinks.forEach(link => {
                    link.classList.remove('active');
                    if (link.getAttribute('href') === `#${sectionId}`) {
                        link.classList.add('active');
                    }
                });
            }
        });
    };
    
    window.addEventListener('scroll', highlightNavigation);
    highlightNavigation(); // Call once on load
    
    // Add syntax highlighting to code blocks
    const codeBlocks = document.querySelectorAll('code');
    codeBlocks.forEach(block => {
        // Simple syntax highlighting for JSON
        if (block.className.includes('language-json')) {
            let html = block.innerHTML;
            // Highlight strings
            html = html.replace(/"([^"]*)"/g, '<span class="string">"$1"</span>');
            // Highlight numbers
            html = html.replace(/\b(\d+)\b/g, '<span class="number">$1</span>');
            // Highlight booleans
            html = html.replace(/\b(true|false)\b/g, '<span class="boolean">$1</span>');
            // Highlight null
            html = html.replace(/\bnull\b/g, '<span class="null">null</span>');
            block.innerHTML = html;
        }
        
        // Simple syntax highlighting for JavaScript
        if (block.className.includes('language-javascript')) {
            let html = block.innerHTML;
            // Highlight keywords
            html = html.replace(/\b(const|let|var|function|async|await|try|catch|if|else|return|throw|new)\b/g, '<span class="keyword">$1</span>');
            // Highlight strings
            html = html.replace(/(['"`])([^'"`]*)(['"`])/g, '<span class="string">$1$2$3</span>');
            // Highlight comments
            html = html.replace(/(\/\/.*$)/gm, '<span class="comment">$1</span>');
            block.innerHTML = html;
        }
        
        // Simple syntax highlighting for Python
        if (block.className.includes('language-python')) {
            let html = block.innerHTML;
            // Highlight keywords
            html = html.replace(/\b(def|class|import|from|if|else|elif|return|try|except|raise|with|as|for|while|in|is|not|and|or)\b/g, '<span class="keyword">$1</span>');
            // Highlight strings
            html = html.replace(/(['"`])([^'"`]*)(['"`])/g, '<span class="string">$1$2$3</span>');
            // Highlight comments
            html = html.replace(/(#.*$)/gm, '<span class="comment">$1</span>');
            block.innerHTML = html;
        }
        
        // Simple syntax highlighting for bash
        if (block.className.includes('language-bash')) {
            let html = block.innerHTML;
            // Highlight strings
            html = html.replace(/(['"`])([^'"`]*)(['"`])/g, '<span class="string">$1$2$3</span>');
            // Highlight comments
            html = html.replace(/(#.*$)/gm, '<span class="comment">$1</span>');
            block.innerHTML = html;
        }
        
        // Simple syntax highlighting for PHP
        if (block.className.includes('language-php')) {
            let html = block.innerHTML;
            // Highlight keywords
            html = html.replace(/\b(function|class|public|private|protected|if|else|elseif|return|try|catch|throw|new|echo|global)\b/g, '<span class="keyword">$1</span>');
            // Highlight variables
            html = html.replace(/(\$\w+)/g, '<span class="variable">$1</span>');
            // Highlight strings
            html = html.replace(/(['"`])([^'"`]*)(['"`])/g, '<span class="string">$1$2$3</span>');
            // Highlight comments
            html = html.replace(/(\/\/.*$)/gm, '<span class="comment">$1</span>');
            block.innerHTML = html;
        }
    });
    
    // Add interactive API testing (optional enhancement)
    const tryButtons = document.querySelectorAll('.try-api-btn');
    tryButtons.forEach(btn => {
        btn.addEventListener('click', async (e) => {
            e.preventDefault();
            const endpoint = btn.dataset.endpoint;
            const method = btn.dataset.method || 'GET';
            
            try {
                const response = await fetch(endpoint, { method });
                const data = await response.json();
                
                // Display result in a modal or inline
                console.log('API Response:', data);
                alert('Check console for API response!');
            } catch (error) {
                console.error('API Error:', error);
                alert('Error calling API. Check console for details.');
            }
        });
    });
});

// Add active class to sidebar navigation
const currentHash = window.location.hash;
if (currentHash) {
    const activeLink = document.querySelector(`.api-nav a[href="${currentHash}"]`);
    if (activeLink) {
        activeLink.classList.add('active');
    }
}