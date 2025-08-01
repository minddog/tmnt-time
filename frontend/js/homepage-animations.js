// Homepage Animations JavaScript

// API Endpoint configurations
const API_BASE = 'https://www.turtletime.dev/api/v1';
const endpoints = {
    'turtles': {
        url: '/turtles',
        example: 'curl https://www.turtletime.dev/api/v1/turtles'
    },
    'random-quote': {
        url: '/quotes/random',
        example: 'curl https://www.turtletime.dev/api/v1/quotes/random'
    },
    'villains': {
        url: '/villains',
        example: 'curl https://www.turtletime.dev/api/v1/villains'
    },
    'weapons': {
        url: '/weapons',
        example: 'curl https://www.turtletime.dev/api/v1/weapons'
    }
};

let currentEndpoint = 'turtles';

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    // Initialize animations
    initializeAnimations();
    
    // Setup API playground
    setupAPIPlayground();
    
    // Setup counter animations
    setupCounterAnimations();
    
    // Setup scroll animations
    setupScrollAnimations();
    
    // Setup hero button actions
    setupHeroButtons();
});

// Initialize all animations
function initializeAnimations() {
    // Trigger animations on elements with data-delay
    const animatedElements = document.querySelectorAll('[data-delay]');
    animatedElements.forEach(element => {
        const delay = element.getAttribute('data-delay');
        element.style.animationDelay = `${delay}ms`;
    });
}

// Setup API Playground
function setupAPIPlayground() {
    // Endpoint selector buttons
    const endpointBtns = document.querySelectorAll('.endpoint-btn');
    endpointBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            // Update active state
            endpointBtns.forEach(b => b.classList.remove('active'));
            this.classList.add('active');
            
            // Update current endpoint
            currentEndpoint = this.getAttribute('data-endpoint');
            updateAPIDisplay();
        });
    });
    
    // Execute button
    const executeBtn = document.getElementById('executeApiBtn');
    if (executeBtn) {
        executeBtn.addEventListener('click', executeAPIRequest);
    }
    
    // Initial display
    updateAPIDisplay();
}

// Update API display based on selected endpoint
function updateAPIDisplay() {
    const endpoint = endpoints[currentEndpoint];
    const urlElement = document.getElementById('apiUrl');
    const codeElement = document.getElementById('codeExample');
    const responseBody = document.getElementById('responseBody');
    const statusCode = document.getElementById('statusCode');
    const responseTime = document.getElementById('responseTime');
    
    if (urlElement && codeElement && endpoint) {
        urlElement.textContent = API_BASE + endpoint.url;
        codeElement.textContent = endpoint.example;
        
        // Clear previous response when switching endpoints
        if (responseBody) {
            responseBody.innerHTML = '<code>Click "Execute Request" to see the live response...</code>';
        }
        if (statusCode) {
            statusCode.textContent = '200 OK';
            statusCode.style.color = '#4CAF50';
        }
        if (responseTime) {
            responseTime.textContent = '';
        }
    }
}

// Execute API request
async function executeAPIRequest() {
    const executeBtn = document.getElementById('executeApiBtn');
    const responseBody = document.getElementById('responseBody');
    const statusCode = document.getElementById('statusCode');
    const responseTime = document.getElementById('responseTime');
    
    // Show loading state
    executeBtn.innerHTML = '<span class="loading"></span> <span>Loading...</span>';
    executeBtn.disabled = true;
    
    const startTime = performance.now();
    
    try {
        const response = await fetch(API_BASE + endpoints[currentEndpoint].url);
        const data = await response.json();
        const endTime = performance.now();
        
        // Update response display
        statusCode.textContent = `${response.status} ${response.statusText}`;
        statusCode.style.color = response.ok ? '#4CAF50' : '#F44336';
        responseTime.textContent = `${Math.round(endTime - startTime)}ms`;
        
        // Pretty print JSON with proper escaping
        const jsonString = JSON.stringify(data, null, 2);
        const escapedJson = jsonString
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;');
        
        responseBody.innerHTML = `<code>${escapedJson}</code>`;
        
        // Add syntax highlighting effect
        highlightJSON(responseBody);
        
    } catch (error) {
        statusCode.textContent = 'Error';
        statusCode.style.color = '#F44336';
        responseBody.innerHTML = `<code style="color: #F44336;">Error: ${error.message}</code>`;
    } finally {
        // Reset button
        executeBtn.innerHTML = '<span class="execute-icon">▶</span> <span>Execute Request</span>';
        executeBtn.disabled = false;
    }
}

// Simple JSON syntax highlighting
function highlightJSON(element) {
    let html = element.innerHTML;
    
    // Highlight strings
    html = html.replace(/"([^"]+)":/g, '<span style="color: #9CDCFE;">"$1"</span>:');
    html = html.replace(/: "([^"]+)"/g, ': <span style="color: #CE9178;">"$1"</span>');
    
    // Highlight numbers
    html = html.replace(/: (\d+)/g, ': <span style="color: #B5CEA8;">$1</span>');
    
    // Highlight booleans and null
    html = html.replace(/: (true|false|null)/g, ': <span style="color: #569CD6;">$1</span>');
    
    element.innerHTML = html;
}

// Copy API URL to clipboard
window.copyApiUrl = function() {
    const urlElement = document.getElementById('apiUrl');
    const copyBtn = event.target;
    
    navigator.clipboard.writeText(urlElement.textContent).then(() => {
        const originalText = copyBtn.textContent;
        copyBtn.textContent = '✅ Copied!';
        setTimeout(() => {
            copyBtn.textContent = originalText;
        }, 2000);
    });
};

// Try example endpoint
window.tryExample = function(endpoint) {
    // Update the playground with the example endpoint
    const endpointKey = Object.keys(endpoints).find(key => 
        endpoints[key].url === '/' + endpoint || 
        endpoints[key].url === '/' + endpoint.split('?')[0]
    );
    
    if (endpointKey) {
        // Find and click the corresponding endpoint button
        const btn = document.querySelector(`[data-endpoint="${endpointKey}"]`);
        if (btn) {
            btn.click();
            
            // Scroll to playground
            document.querySelector('.api-playground').scrollIntoView({ 
                behavior: 'smooth', 
                block: 'center' 
            });
            
            // Auto-execute after scroll
            setTimeout(() => {
                document.getElementById('executeApiBtn').click();
            }, 800);
        }
    }
};

// Setup counter animations
function setupCounterAnimations() {
    const observerOptions = {
        threshold: 0.5,
        rootMargin: '0px'
    };
    
    const counterObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const counter = entry.target;
                const target = parseInt(counter.getAttribute('data-count'));
                animateCounter(counter, target);
                counterObserver.unobserve(counter);
            }
        });
    }, observerOptions);
    
    // Observe all counters
    document.querySelectorAll('.stat-number').forEach(counter => {
        counterObserver.observe(counter);
    });
}

// Animate counter from 0 to target
function animateCounter(element, target) {
    let current = 0;
    const increment = target / 50;
    const timer = setInterval(() => {
        current += increment;
        if (current >= target) {
            current = target;
            clearInterval(timer);
        }
        element.textContent = Math.floor(current);
    }, 30);
}

// Setup scroll-triggered animations
function setupScrollAnimations() {
    const animationObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.animationPlayState = 'running';
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '50px'
    });
    
    // Observe all animated elements
    const animatedElements = document.querySelectorAll('.slide-in, .fade-in, .zoom-in, .slide-up, .rotate-in, .bounce-in');
    animatedElements.forEach(element => {
        element.style.animationPlayState = 'paused';
        animationObserver.observe(element);
    });
}

// Setup hero button actions
function setupHeroButtons() {
    const tryApiBtn = document.getElementById('tryApiBtn');
    if (tryApiBtn) {
        tryApiBtn.addEventListener('click', () => {
            // Scroll to API playground
            document.querySelector('.api-playground').scrollIntoView({ 
                behavior: 'smooth', 
                block: 'center' 
            });
            
            // Execute a request after scrolling
            setTimeout(() => {
                document.getElementById('executeApiBtn').click();
            }, 800);
        });
    }
}

// Add some fun particle effects on mouse move
let mouseX = 0;
let mouseY = 0;

document.addEventListener('mousemove', (e) => {
    mouseX = e.clientX;
    mouseY = e.clientY;
});

// Parallax effect for floating turtles
function updateParallax() {
    const turtles = document.querySelectorAll('.floating-turtle');
    turtles.forEach((turtle, index) => {
        const speed = 0.02 * (index + 1);
        const x = (window.innerWidth / 2 - mouseX) * speed;
        const y = (window.innerHeight / 2 - mouseY) * speed;
        
        turtle.style.transform = `translate(${x}px, ${y}px)`;
    });
    
    requestAnimationFrame(updateParallax);
}

// Start parallax animation
updateParallax();

// Add keyboard shortcuts
document.addEventListener('keydown', (e) => {
    // Press 'T' to try the API
    if (e.key.toLowerCase() === 't' && !e.ctrlKey && !e.metaKey) {
        const tryApiBtn = document.getElementById('tryApiBtn');
        if (tryApiBtn) tryApiBtn.click();
    }
    
    // Press numbers 1-4 to switch endpoints
    if (e.key >= '1' && e.key <= '4') {
        const index = parseInt(e.key) - 1;
        const btns = document.querySelectorAll('.endpoint-btn');
        if (btns[index]) btns[index].click();
    }
});

// Add some console easter eggs
console.log('%c🐢 COWABUNGA! 🐢', 'color: #4CAF50; font-size: 24px; font-weight: bold;');
console.log('%cWelcome to the TMNT API!', 'color: #2196F3; font-size: 16px;');
console.log('%cTry pressing "T" to test the API or use number keys 1-4 to switch endpoints!', 'color: #FF9800; font-size: 14px;');