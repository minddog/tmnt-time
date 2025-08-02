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
            <div class="turtle-image-container">
                <img src="${turtle.image_url}" alt="${turtle.full_name}" class="turtle-image">
            </div>
            <div class="turtle-info">
                <h2>${turtle.full_name}</h2>
                <span class="color-badge ${turtle.color}">${turtle.color.toUpperCase()}</span>
                <p><strong>Weapon:</strong> ${turtle.weapon}</p>
                <p><strong>Personality:</strong> ${turtle.personality}</p>
                <p><strong>Favorite Pizza:</strong> ${turtle.favorite_pizza}</p>
                <p><em>"${turtle.catchphrase}"</em></p>
            </div>
        </div>
    `).join('');

    // Add click handlers for modal
    document.querySelectorAll('.turtle-card').forEach(card => {
        card.addEventListener('click', () => {
            const turtleName = card.dataset.turtle;
            showTurtleModal(turtleName);
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

async function showTurtleModal(turtleName) {
    const modal = document.getElementById('turtleModal');
    const modalContent = document.getElementById('turtleModalContent');
    const turtle = await fetchAPI(`/turtles/${turtleName}`);

    if (turtle && modal && modalContent) {
        modalContent.innerHTML = `
            <div class="modal-header turtle-modal-header ${turtle.name}">
                <div class="modal-turtle-image">
                    <img src="${turtle.image_url}" alt="${turtle.full_name}">
                </div>
                <div class="modal-turtle-title">
                    <h2>${turtle.full_name}</h2>
                    <span class="color-badge ${turtle.color}">${turtle.color.toUpperCase()}</span>
                </div>
            </div>
            <div class="modal-body">
                <div class="modal-section">
                    <h3>Profile</h3>
                    <p><strong>Weapon of Choice:</strong> ${turtle.weapon}</p>
                    <p><strong>Personality:</strong> ${turtle.personality}</p>
                    <p><strong>Favorite Pizza:</strong> ${turtle.favorite_pizza}</p>
                </div>
                
                <div class="modal-section">
                    <h3>Signature Catchphrase</h3>
                    <p class="catchphrase">"${turtle.catchphrase}"</p>
                </div>
                
                <div class="modal-section">
                    <h3>About ${turtle.full_name.split(' ')[0]}</h3>
                    <p>${getTurtleDescription(turtle.name)}</p>
                </div>
            </div>
        `;
        modal.style.display = 'block';
        document.body.style.overflow = 'hidden'; // Prevent background scrolling
    }
}

function getTurtleDescription(name) {
    const descriptions = {
        leonardo: "The eldest and most disciplined of the four brothers, Leonardo serves as the team's leader. His dedication to ninjutsu and unwavering sense of responsibility often puts him at odds with his more carefree brothers, but his tactical mind and cool head under pressure make him an invaluable asset in battle.",
        donatello: "The genius inventor and tech expert of the team, Donatello combines his mastery of the bo staff with an incredible aptitude for science and technology. His inventions and gadgets often give the turtles the edge they need against their technologically advanced enemies.",
        raphael: "Hot-headed and aggressive, Raphael is the team's powerhouse. His twin sai and fierce fighting style make him a formidable opponent, though his temper sometimes gets the better of him. Despite his rough exterior, he deeply cares for his brothers and would do anything to protect them.",
        michelangelo: "The youngest and most lighthearted of the brothers, Michelangelo brings levity to even the darkest situations. His mastery of the nunchaku is matched only by his love of pizza and terrible jokes. While others may underestimate him due to his playful nature, his natural agility and unpredictability make him a skilled warrior."
    };
    return descriptions[name] || "A skilled ninja turtle and valued member of the team.";
}

// Villains page functionality
async function loadVillains() {
    const container = document.getElementById('villainsContainer');
    if (!container) return;

    const villains = await fetchAPI('/villains');
    if (villains) {
        container.innerHTML = villains.map(villain => `
            <div class="villain-card" data-villain="${villain.name}">
                <div class="villain-image-container">
                    <img src="${villain.image_url}" alt="${villain.name}" class="villain-image">
                </div>
                <div class="villain-info">
                    <h2>${villain.name.replace(/_/g, ' ').toUpperCase()}</h2>
                    ${villain.real_name ? `<p><em>Real Name: ${villain.real_name}</em></p>` : ''}
                    <p>${villain.description}</p>
                    <div class="villain-abilities">
                        ${villain.abilities.map(ability => 
                            `<span class="ability-tag">${ability}</span>`
                        ).join('')}
                    </div>
                    <p><small>First Appearance: ${villain.first_appearance}</small></p>
                    ${villain.threat_level ? `<p class="threat-level">Threat Level: <span class="threat-${villain.threat_level.toLowerCase()}">${villain.threat_level}</span></p>` : ''}
                </div>
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
            <div class="modal-header">
                <div class="modal-villain-image">
                    <img src="${villain.image_url}" alt="${villain.name}">
                </div>
                <div class="modal-villain-title">
                    <h2>${villain.name.replace(/_/g, ' ')}</h2>
                    ${villain.real_name ? `<p>Real Name: ${villain.real_name}</p>` : ''}
                </div>
            </div>
            <div class="modal-body">
                <div class="modal-section">
                    <h3>Description</h3>
                    <p>${villain.description}</p>
                </div>
                
                <div class="modal-section">
                    <h3>Abilities & Powers</h3>
                    <div class="modal-abilities">
                        ${villain.abilities.map(ability => 
                            `<span class="ability-tag">${ability}</span>`
                        ).join('')}
                    </div>
                </div>
                
                <div class="modal-section">
                    <h3>Details</h3>
                    <p><strong>First Appearance:</strong> ${villain.first_appearance}</p>
                    ${villain.threat_level ? `<p><strong>Threat Level:</strong> <span class="threat-${villain.threat_level.toLowerCase()}">${villain.threat_level}</span></p>` : ''}
                    ${villain.arch_enemy_of ? `<p><strong>Arch Enemy of:</strong> ${villain.arch_enemy_of}</p>` : ''}
                </div>
            </div>
        `;
        modal.style.display = 'block';
        document.body.style.overflow = 'hidden'; // Prevent background scrolling
    }
}

async function showEpisodeModal(episodeId) {
    const modal = document.getElementById('episodeModal');
    const modalContent = document.getElementById('episodeModalContent');
    const episode = await fetchAPI(`/episodes/${episodeId}`);

    if (episode && modal && modalContent) {
        // Generate cast list HTML
        const castListHTML = episode.cast && episode.cast.length > 0 ? `
            <div class="modal-section">
                <h3>Voice Cast</h3>
                <div class="cast-grid">
                    ${episode.cast.map(member => `
                        <div class="cast-member ${member.role}">
                            <div class="character-name">${member.character_name}</div>
                            <div class="voice-actor">Voiced by: ${member.voice_actor}</div>
                            <span class="role-badge">${member.role}</span>
                        </div>
                    `).join('')}
                </div>
            </div>
        ` : '';

        modalContent.innerHTML = `
            <div class="modal-header episode-modal-header">
                <div class="episode-modal-info">
                    <h2>${episode.title}</h2>
                    <div class="episode-meta">
                        <span class="episode-badge">Season ${episode.season}, Episode ${episode.episode_number}</span>
                        ${episode.air_date ? `<span class="air-date">Aired: ${episode.air_date}</span>` : ''}
                    </div>
                </div>
            </div>
            <div class="modal-body">
                <div class="modal-section">
                    <h3>Synopsis</h3>
                    <p>${episode.synopsis}</p>
                </div>
                
                ${episode.villains_featured && episode.villains_featured.length > 0 ? `
                    <div class="modal-section">
                        <h3>Featured Villains</h3>
                        <div class="modal-villains">
                            ${episode.villains_featured.map(villain => 
                                `<span class="villain-tag large">${villain}</span>`
                            ).join('')}
                        </div>
                    </div>
                ` : ''}
                
                ${castListHTML}
                
                ${episode.writer || episode.director ? `
                    <div class="modal-section">
                        <h3>Credits</h3>
                        ${episode.writer ? `<p><strong>Written by:</strong> ${episode.writer}</p>` : ''}
                        ${episode.director ? `<p><strong>Directed by:</strong> ${episode.director}</p>` : ''}
                    </div>
                ` : ''}
                
                ${episode.notes ? `
                    <div class="modal-section">
                        <h3>Production Notes</h3>
                        <p>${episode.notes}</p>
                    </div>
                ` : ''}
            </div>
        `;
        modal.style.display = 'block';
        document.body.style.overflow = 'hidden'; // Prevent background scrolling
    }
}

// Modal close functionality
document.addEventListener('DOMContentLoaded', () => {
    const villainModal = document.getElementById('villainModal');
    const turtleModal = document.getElementById('turtleModal');
    const episodeModal = document.getElementById('episodeModal');
    
    // Close button handlers
    document.querySelectorAll('.close').forEach(closeBtn => {
        closeBtn.addEventListener('click', () => {
            const modal = closeBtn.closest('.modal');
            if (modal) {
                modal.style.display = 'none';
                document.body.style.overflow = ''; // Restore scrolling
            }
        });
    });

    // Click outside to close
    window.addEventListener('click', (e) => {
        if (e.target === villainModal || e.target === turtleModal || e.target === episodeModal) {
            e.target.style.display = 'none';
            document.body.style.overflow = ''; // Restore scrolling
        }
    });
});

// Episodes page functionality
let currentView = 'table'; // Default view

async function loadEpisodes(season = null, offset = 0) {
    const container = document.getElementById('episodesContainer');
    if (!container) return;

    let endpoint = `/episodes?limit=${itemsPerPage}&offset=${offset}`;
    if (season) {
        endpoint += `&season=${season}`;
    }

    const episodes = await fetchAPI(endpoint);
    if (episodes) {
        if (currentView === 'table') {
            displayEpisodesTable(episodes, container);
        } else {
            displayEpisodesCards(episodes, container);
        }
        updatePagination(episodes.length);
    }
}

function displayEpisodesCards(episodes, container) {
    container.innerHTML = episodes.map(episode => `
        <div class="episode-card" data-episode-id="${episode.id || episode.episode_id}">
            <div class="episode-header">
                <h3 class="episode-title">${episode.title}</h3>
                <span class="episode-info">S${episode.season}E${episode.episode_number}</span>
            </div>
            ${episode.air_date ? `<p class="episode-date">Aired: ${episode.air_date}</p>` : ''}
            <p class="episode-synopsis">${episode.synopsis}</p>
            ${episode.villains_featured && episode.villains_featured.length > 0 ? `
                <div class="episode-villains">
                    <strong>Featured Villains:</strong>
                    ${episode.villains_featured.map(villain => 
                        `<span class="villain-tag">${villain}</span>`
                    ).join('')}
                </div>
            ` : ''}
            <div class="episode-actions">
                <button class="btn btn-small btn-secondary quick-view-btn" data-episode-id="${episode.id || episode.episode_id}">
                    <span>Quick View</span>
                </button>
                <a href="/pages/episode-detail.html?id=${episode.id || episode.episode_id}" class="btn btn-small btn-primary">
                    <span>Full Details →</span>
                </a>
            </div>
        </div>
    `).join('');

    // Add click handlers for modal on the quick view button
    document.querySelectorAll('.quick-view-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.stopPropagation(); // Prevent card click
            const episodeId = btn.dataset.episodeId;
            showEpisodeModal(episodeId);
        });
    });
}

function displayEpisodesTable(episodes, container) {
    container.innerHTML = `
        <div class="episodes-table-container">
            <table class="episodes-table">
                <thead>
                    <tr>
                        <th>Episode</th>
                        <th>Title</th>
                        <th>Air Date</th>
                        <th>Synopsis</th>
                        <th>Villains</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    ${episodes.map(episode => `
                        <tr>
                            <td class="episode-number-cell">
                                S${episode.season}E${episode.episode_number}
                            </td>
                            <td class="episode-title-cell">
                                <a href="/pages/episode-detail.html?id=${episode.id || episode.episode_id}" class="episode-title-link">
                                    ${episode.title}
                                </a>
                            </td>
                            <td class="episode-date-cell">
                                ${episode.air_date || 'N/A'}
                            </td>
                            <td class="episode-synopsis-cell">
                                ${episode.synopsis.length > 150 ? 
                                    episode.synopsis.substring(0, 150) + '...' : 
                                    episode.synopsis}
                            </td>
                            <td class="episode-villains-cell">
                                ${episode.villains_featured && episode.villains_featured.length > 0 ? 
                                    episode.villains_featured.map(villain => 
                                        `<span class="villain-badge">${villain}</span>`
                                    ).join('') : 
                                    '-'
                                }
                            </td>
                            <td class="episode-actions-cell">
                                <button class="btn btn-small btn-secondary quick-view-btn" data-episode-id="${episode.id || episode.episode_id}">
                                    Quick View
                                </button>
                                <a href="/pages/episode-detail.html?id=${episode.id || episode.episode_id}" class="btn btn-small btn-primary">
                                    Full Details
                                </a>
                            </td>
                        </tr>
                    `).join('')}
                </tbody>
            </table>
        </div>
    `;

    // Add click handlers for modal on the quick view button
    document.querySelectorAll('.quick-view-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.stopPropagation();
            const episodeId = btn.dataset.episodeId;
            showEpisodeModal(episodeId);
        });
    });
}

function setupEpisodeFilters() {
    const seasonFilter = document.getElementById('seasonFilter');
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const tableViewBtn = document.getElementById('tableViewBtn');
    const cardViewBtn = document.getElementById('cardViewBtn');

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

    // View toggle functionality
    if (tableViewBtn && cardViewBtn) {
        tableViewBtn.addEventListener('click', () => {
            if (currentView !== 'table') {
                currentView = 'table';
                tableViewBtn.classList.add('active');
                cardViewBtn.classList.remove('active');
                const season = seasonFilter?.value || null;
                loadEpisodes(season, (currentPage - 1) * itemsPerPage);
            }
        });

        cardViewBtn.addEventListener('click', () => {
            if (currentView !== 'cards') {
                currentView = 'cards';
                cardViewBtn.classList.add('active');
                tableViewBtn.classList.remove('active');
                const season = seasonFilter?.value || null;
                loadEpisodes(season, (currentPage - 1) * itemsPerPage);
            }
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

