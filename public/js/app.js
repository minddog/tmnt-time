// API Base URL - will work both locally and on Vercel
const API_BASE_URL = '/api/v1';

// Global state
let currentPage = 1;
const itemsPerPage = 10;

// Utility function for API calls
async function fetchAPI(endpoint) {
    try {
        const response = await fetch(`${API_BASE_URL}${endpoint}`);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return await response.json();
    } catch (error) {
        console.error('API fetch error:', error);
        return null;
    }
}

// Navigation menu toggle for mobile
document.addEventListener('DOMContentLoaded', () => {
    const hamburger = document.querySelector('.hamburger');
    const navMenu = document.querySelector('.nav-menu');

    if (hamburger) {
        hamburger.addEventListener('click', () => {
            navMenu.classList.toggle('active');
        });
    }

    // Close mobile menu when clicking outside
    document.addEventListener('click', (e) => {
        if (!hamburger.contains(e.target) && !navMenu.contains(e.target)) {
            navMenu.classList.remove('active');
        }
    });
});

// Homepage functionality
if (document.getElementById('randomQuoteBtn')) {
    const quoteBtn = document.getElementById('randomQuoteBtn');
    const quoteDisplay = document.getElementById('quoteDisplay');

    quoteBtn.addEventListener('click', async () => {
        const quote = await fetchAPI('/quotes/random');
        if (quote) {
            quoteDisplay.innerHTML = `
                <blockquote>
                    <p>"${quote.text}"</p>
                    <footer>- ${quote.character}</footer>
                </blockquote>
            `;
            quoteDisplay.classList.add('show');
        }
    });

    // Load weapons on homepage
    loadWeapons();

    // Setup search functionality
    setupSearch();
}

// Load weapons for homepage
async function loadWeapons() {
    const weaponsContainer = document.getElementById('weaponsContainer');
    if (!weaponsContainer) return;

    const weapons = await fetchAPI('/weapons');
    if (weapons) {
        weaponsContainer.innerHTML = weapons.map(weapon => `
            <div class="weapon-card">
                <h3 class="weapon-name">${weapon.name}</h3>
                <p class="weapon-wielder">Wielder: ${weapon.wielder}</p>
                <p class="weapon-type">Type: ${weapon.type}</p>
                <p>${weapon.description}</p>
                ${weapon.special_moves.length > 0 ? `
                    <div class="special-moves">
                        <strong>Special Moves:</strong>
                        <ul>
                            ${weapon.special_moves.map(move => `<li>${move}</li>`).join('')}
                        </ul>
                    </div>
                ` : ''}
            </div>
        `).join('');
    }
}

// Search functionality
function setupSearch() {
    const searchInput = document.getElementById('searchInput');
    const searchBtn = document.getElementById('searchBtn');
    const searchResults = document.getElementById('searchResults');

    if (!searchInput || !searchBtn) return;

    const performSearch = async () => {
        const query = searchInput.value.trim();
        if (query.length < 2) {
            alert('Please enter at least 2 characters to search');
            return;
        }

        const results = await fetchAPI(`/search?q=${encodeURIComponent(query)}`);
        if (results) {
            displaySearchResults(results, searchResults);
        }
    };

    searchBtn.addEventListener('click', performSearch);
    searchInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') performSearch();
    });
}

function displaySearchResults(results, container) {
    let html = '';

    if (results.turtles.length > 0) {
        html += `
            <div class="search-result-section">
                <h3>Turtles</h3>
                ${results.turtles.map(turtle => `
                    <div class="search-result-item">
                        <strong>${turtle.full_name}</strong> - ${turtle.personality}
                    </div>
                `).join('')}
            </div>
        `;
    }

    if (results.villains.length > 0) {
        html += `
            <div class="search-result-section">
                <h3>Villains</h3>
                ${results.villains.map(villain => `
                    <div class="search-result-item">
                        <strong>${villain.name}</strong> - ${villain.description}
                    </div>
                `).join('')}
            </div>
        `;
    }

    if (results.episodes.length > 0) {
        html += `
            <div class="search-result-section">
                <h3>Episodes</h3>
                ${results.episodes.map(episode => `
                    <div class="search-result-item">
                        <strong>${episode.title}</strong> - ${episode.synopsis}
                    </div>
                `).join('')}
            </div>
        `;
    }

    if (results.quotes.length > 0) {
        html += `
            <div class="search-result-section">
                <h3>Quotes</h3>
                ${results.quotes.map(quote => `
                    <div class="search-result-item">
                        "${quote.text}" - <em>${quote.character}</em>
                    </div>
                `).join('')}
            </div>
        `;
    }

    container.innerHTML = html || '<p>No results found.</p>';
}

// Turtles page functionality
async function loadTurtles() {
    const container = document.getElementById('turtlesContainer');
    if (!container) return;

    const turtles = await fetchAPI('/turtles');
    if (turtles) {
        displayTurtles(turtles, container);
    }
}

function displayTurtles(turtles, container) {
    container.innerHTML = turtles.map(turtle => `
        <div class="turtle-card ${turtle.name}" data-turtle="${turtle.name}">
            <img src="${turtle.image_url}" alt="${turtle.full_name}" class="turtle-image" loading="lazy">
            <h2>${turtle.full_name}</h2>
            <span class="color-badge ${turtle.color}">${turtle.color.toUpperCase()}</span>
            <p><strong>Weapon:</strong> ${turtle.weapon}</p>
            <p><strong>Personality:</strong> ${turtle.personality}</p>
            <p><strong>Favorite Pizza:</strong> ${turtle.favorite_pizza}</p>
            <p><em>"${turtle.catchphrase}"</em></p>
        </div>
    `).join('');

    // Add click handlers
    document.querySelectorAll('.turtle-card').forEach(card => {
        card.addEventListener('click', () => {
            const turtleName = card.dataset.turtle;
            showTurtleDetail(turtleName);
        });
    });
}

function setupTurtleFilters() {
    const buttons = document.querySelectorAll('.turtle-btn');
    const container = document.getElementById('turtlesContainer');

    buttons.forEach(btn => {
        btn.addEventListener('click', async () => {
            // Update active state
            buttons.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            const filter = btn.dataset.turtle;
            
            if (filter === 'all') {
                const turtles = await fetchAPI('/turtles');
                if (turtles) displayTurtles(turtles, container);
            } else {
                const turtle = await fetchAPI(`/turtles/${filter}`);
                if (turtle) displayTurtles([turtle], container);
            }
        });
    });
}

async function showTurtleDetail(turtleName) {
    const modal = document.getElementById('turtleModal');
    const modalContent = document.getElementById('turtleModalContent');
    const turtle = await fetchAPI(`/turtles/${turtleName}`);
    
    if (turtle && modal && modalContent) {
        // Get weapon stats based on turtle
        const weaponStats = getWeaponStats(turtle.weapon);
        
        modalContent.innerHTML = `
            <div class="turtle-modal-hero ${turtle.name}">
                <img src="${turtle.image_url}" alt="${turtle.full_name}" class="turtle-modal-image">
                <div class="turtle-particles"></div>
            </div>
            <div class="turtle-modal-details">
                <h2 class="turtle-modal-name">${turtle.full_name}</h2>
                <span class="turtle-modal-badge ${turtle.color}">${turtle.color.toUpperCase()} NINJA</span>
                
                <div class="turtle-stats">
                    <div class="stat-item">
                        <span class="stat-label">Weapon</span>
                        <span class="stat-value">${turtle.weapon}</span>
                    </div>
                    <div class="stat-item">
                        <span class="stat-label">Pizza</span>
                        <span class="stat-value">${turtle.favorite_pizza}</span>
                    </div>
                </div>
                
                <div class="weapon-abilities">
                    <h3>Weapon Abilities</h3>
                    <div class="ability-bars">
                        <div class="ability-bar">
                            <span>Power</span>
                            <div class="bar-bg">
                                <div class="bar-fill ${turtle.color}" style="width: ${weaponStats.power}%"></div>
                            </div>
                        </div>
                        <div class="ability-bar">
                            <span>Speed</span>
                            <div class="bar-bg">
                                <div class="bar-fill ${turtle.color}" style="width: ${weaponStats.speed}%"></div>
                            </div>
                        </div>
                        <div class="ability-bar">
                            <span>Range</span>
                            <div class="bar-bg">
                                <div class="bar-fill ${turtle.color}" style="width: ${weaponStats.range}%"></div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <p class="turtle-personality"><strong>Personality:</strong> ${turtle.personality}</p>
                
                <div class="turtle-catchphrase">
                    <span class="quote-mark">"</span>
                    ${turtle.catchphrase}
                    <span class="quote-mark">"</span>
                </div>
                
                <button class="action-btn ${turtle.color}" onclick="playTurtleSound('${turtle.name}')">
                    🔊 Hear Battle Cry!
                </button>
            </div>
        `;
        
        // Show modal with animation
        modal.style.display = 'block';
        setTimeout(() => modal.classList.add('show'), 10);
        
        // Add particle effects
        createParticles(turtle.color);
    }
}

// Villains page functionality
async function loadVillains() {
    const container = document.getElementById('villainsContainer');
    if (!container) return;

    const villains = await fetchAPI('/villains');
    if (villains) {
        container.innerHTML = villains.map(villain => `
            <div class="villain-card" data-villain="${villain.name}">
                <img src="${villain.image_url}" alt="${villain.name}" class="villain-image" loading="lazy">
                <h2>${villain.name.replace(/_/g, ' ').toUpperCase()}</h2>
                ${villain.real_name ? `<p><em>Real Name: ${villain.real_name}</em></p>` : ''}
                <p>${villain.description}</p>
                <div class="villain-abilities">
                    ${villain.abilities.map(ability => 
                        `<span class="ability-tag">${ability}</span>`
                    ).join('')}
                </div>
                <p><small>First Appearance: ${villain.first_appearance}</small></p>
            </div>
        `).join('');

        // Add click handlers for modal
        document.querySelectorAll('.villain-card').forEach(card => {
            card.addEventListener('click', () => {
                const villainName = card.dataset.villain;
                showVillainModal(villainName);
            });
        });
    }
}

async function showVillainModal(villainName) {
    const modal = document.getElementById('villainModal');
    const modalContent = document.getElementById('villainModalContent');
    const villain = await fetchAPI(`/villains/${villainName}`);

    if (villain && modal && modalContent) {
        modalContent.innerHTML = `
            <h2>${villain.name.replace(/_/g, ' ').toUpperCase()}</h2>
            ${villain.real_name ? `<p><strong>Real Name:</strong> ${villain.real_name}</p>` : ''}
            <p><strong>Description:</strong> ${villain.description}</p>
            <div>
                <strong>Abilities:</strong>
                <ul>
                    ${villain.abilities.map(ability => `<li>${ability}</li>`).join('')}
                </ul>
            </div>
            <p><strong>First Appearance:</strong> ${villain.first_appearance}</p>
            ${villain.arch_enemy_of ? `<p><strong>Arch Enemy of:</strong> ${villain.arch_enemy_of}</p>` : ''}
        `;
        modal.style.display = 'block';
    }
}

// Modal close functionality
document.addEventListener('DOMContentLoaded', () => {
    const modal = document.getElementById('villainModal');
    const closeBtn = document.querySelector('.close');

    if (closeBtn) {
        closeBtn.addEventListener('click', () => {
            modal.style.display = 'none';
        });
    }

    window.addEventListener('click', (e) => {
        if (e.target === modal) {
            modal.style.display = 'none';
        }
    });
});

// Episodes page functionality
async function loadEpisodes(season = null, offset = 0) {
    const container = document.getElementById('episodesContainer');
    if (!container) return;

    let endpoint = `/episodes?limit=${itemsPerPage}&offset=${offset}`;
    if (season) {
        endpoint += `&season=${season}`;
    }

    const episodes = await fetchAPI(endpoint);
    if (episodes) {
        displayEpisodes(episodes, container);
        updatePagination(episodes.length);
    }
}

function displayEpisodes(episodes, container) {
    container.innerHTML = episodes.map(episode => `
        <div class="episode-card">
            <div class="episode-header">
                <h3 class="episode-title">${episode.title}</h3>
                <span class="episode-info">S${episode.season}E${episode.episode_number}</span>
            </div>
            ${episode.air_date ? `<p class="episode-date">Aired: ${episode.air_date}</p>` : ''}
            <p class="episode-synopsis">${episode.synopsis}</p>
            ${episode.villains_featured.length > 0 ? `
                <div class="episode-villains">
                    <strong>Featured Villains:</strong>
                    ${episode.villains_featured.map(villain => 
                        `<span class="villain-tag">${villain}</span>`
                    ).join('')}
                </div>
            ` : ''}
        </div>
    `).join('');
}

function setupEpisodeFilters() {
    const seasonFilter = document.getElementById('seasonFilter');
    const searchInput = document.getElementById('episodeSearch');
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');

    if (seasonFilter) {
        seasonFilter.addEventListener('change', () => {
            currentPage = 1;
            const season = seasonFilter.value || null;
            loadEpisodes(season, 0);
        });
    }

    if (prevBtn && nextBtn) {
        prevBtn.addEventListener('click', () => {
            if (currentPage > 1) {
                currentPage--;
                const season = seasonFilter?.value || null;
                loadEpisodes(season, (currentPage - 1) * itemsPerPage);
            }
        });

        nextBtn.addEventListener('click', () => {
            currentPage++;
            const season = seasonFilter?.value || null;
            loadEpisodes(season, (currentPage - 1) * itemsPerPage);
        });
    }

    if (searchInput) {
        searchInput.addEventListener('input', debounce(async (e) => {
            const query = e.target.value.trim();
            if (query.length >= 2) {
                const results = await fetchAPI(`/search?q=${encodeURIComponent(query)}`);
                if (results && results.episodes.length > 0) {
                    const container = document.getElementById('episodesContainer');
                    displayEpisodes(results.episodes, container);
                }
            } else if (query.length === 0) {
                loadEpisodes();
            }
        }, 300));
    }
}

function updatePagination(itemCount) {
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const pageInfo = document.getElementById('pageInfo');

    if (prevBtn) prevBtn.disabled = currentPage === 1;
    if (nextBtn) nextBtn.disabled = itemCount < itemsPerPage;
    if (pageInfo) pageInfo.textContent = `Page ${currentPage}`;
}

// Utility function for debouncing
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Helper functions for turtle modal
function getWeaponStats(weapon) {
    const stats = {
        'Katana': { power: 85, speed: 90, range: 70 },
        'Bo Staff': { power: 70, speed: 75, range: 95 },
        'Sai': { power: 80, speed: 85, range: 50 },
        'Nunchucks': { power: 75, speed: 95, range: 60 }
    };
    return stats[weapon] || { power: 50, speed: 50, range: 50 };
}

function createParticles(color) {
    const container = document.querySelector('.turtle-particles');
    if (!container) return;
    
    container.innerHTML = '';
    const colors = {
        'blue': '#1e3a8a',
        'purple': '#7c3aed',
        'red': '#dc2626',
        'orange': '#f97316'
    };
    
    for (let i = 0; i < 20; i++) {
        const particle = document.createElement('div');
        particle.className = 'particle';
        particle.style.background = colors[color];
        particle.style.left = Math.random() * 100 + '%';
        particle.style.animationDelay = Math.random() * 2 + 's';
        particle.style.animationDuration = (2 + Math.random() * 3) + 's';
        container.appendChild(particle);
    }
}

function playTurtleSound(turtleName) {
    // Simulate sound effect with visual feedback
    const btn = event.target;
    btn.textContent = '🎵 ' + (turtleName === 'michelangelo' ? 'COWABUNGA!' : 'TURTLE POWER!');
    btn.disabled = true;
    
    setTimeout(() => {
        btn.textContent = '🔊 Hear Battle Cry!';
        btn.disabled = false;
    }, 2000);
}

// Setup modal close handlers
document.addEventListener('DOMContentLoaded', () => {
    const modal = document.getElementById('turtleModal');
    const closeBtn = document.querySelector('.close-modal');
    
    if (closeBtn) {
        closeBtn.onclick = () => {
            modal.classList.remove('show');
            setTimeout(() => modal.style.display = 'none', 300);
        };
    }
    
    if (modal) {
        window.onclick = (event) => {
            if (event.target === modal) {
                modal.classList.remove('show');
                setTimeout(() => modal.style.display = 'none', 300);
            }
        };
    }
});