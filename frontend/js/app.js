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
    const detailDiv = document.getElementById('turtleDetail');
    const turtle = await fetchAPI(`/turtles/${turtleName}`);
    
    if (turtle && detailDiv) {
        detailDiv.innerHTML = `
            <div class="turtle-detail-content">
                <h2>${turtle.full_name}</h2>
                <div class="turtle-detail-info">
                    <p><strong>Color:</strong> ${turtle.color}</p>
                    <p><strong>Weapon:</strong> ${turtle.weapon}</p>
                    <p><strong>Personality:</strong> ${turtle.personality}</p>
                    <p><strong>Favorite Pizza:</strong> ${turtle.favorite_pizza}</p>
                    <p><strong>Catchphrase:</strong> "${turtle.catchphrase}"</p>
                </div>
            </div>
        `;
        detailDiv.classList.remove('hidden');
        
        // Scroll to detail
        detailDiv.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
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

}

function updatePagination(itemCount) {
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const pageInfo = document.getElementById('pageInfo');

    if (prevBtn) prevBtn.disabled = currentPage === 1;
    if (nextBtn) nextBtn.disabled = itemCount < itemsPerPage;
    if (pageInfo) pageInfo.textContent = `Page ${currentPage}`;
}

