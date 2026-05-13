const API_URL = "http://localhost:8010/api";
let allHeroes = [];
let selectedRating = 0;
let currentHeroForReview = "";

function navigateTo(pageKey) {
    document.querySelectorAll('.page').forEach(p => p.classList.add('hidden'));

    document.querySelectorAll('.nav-links a').forEach(a => a.classList.remove('active'));

    const targetPage = document.getElementById(`${pageKey}-section`);
    if (targetPage) {
        targetPage.classList.remove('hidden');
    }

    const targetLink = document.getElementById(`link-${pageKey}`);
    if (targetLink) {
        targetLink.classList.add('active');
    }

    // Вызов загрузки данных в зависимости от страницы
    if (pageKey === 'home') loadTopHeroes();
    if (pageKey === 'heroes') loadHeroes();
    if (pageKey === 'reviews') loadAllReviews();
}

async function loadTopHeroes() {
    try {
        const res = await fetch(`${API_URL}/heroes/top`);
        const top = await res.json();
        const container = document.getElementById('top-list');

        if (top.length === 0) {
            container.innerHTML = '<span class="no-reviews">Стань первым, кто оставит отзыв!</span>';
            return;
        }

        container.innerHTML = top.map(h => `
            <div class="top-item">${h.name} <span>${h.count} ОТЗ.</span></div>
        `).join('');
    } catch (e) { console.error("Ошибка ТОПа"); }
}

async function loadHeroes() {
    try {
        const res = await fetch(`${API_URL}/heroes`);
        allHeroes = await res.json();
        applyAllFilters();
    } catch (e) { console.error("Ошибка героев"); }
}

function applyAllFilters() {
    const search = document.getElementById('hero-search').value.toLowerCase();
    const filter = document.getElementById('attribute-filter').value;

    const filtered = allHeroes.filter(h => {
        const matchesSearch = h.name.toLowerCase().includes(search);
        if (filter === 'all') return matchesSearch;
        const [key, val] = filter.split(':');
        return matchesSearch && h[key] === val;
    });

    const list = document.getElementById('heroes-list');
    list.innerHTML = filtered.map(h => `
        <div class="hero-row-grid">
            <div class="hero-name-cell">${h.name}</div>
            <div style="color:#555; font-size: 12px; text-transform: uppercase; letter-spacing: 1px;">${h.attack_type}</div>
            <div style="color:#777; font-family: 'Roboto Condensed';">${h.description}</div>
            <div style="font-weight: 700; font-size: 14px; color: ${
                h.difficulty === 'Easy' ? '#2ecc71' : h.difficulty === 'Medium' ? '#f1c40f' : '#e74c3c'
            }">${h.difficulty.toUpperCase()}</div>
            <div class="rating-cell">${h.avg_rating > 0 ? '★ ' + h.avg_rating : '—'}</div>
            <div class="action-col">
                <button class="table-action-btn" onclick="openReviewForm('${h.name}')">ОТЗЫВ</button>
            </div>
        </div>
    `).join('');
}

function setRating(val) {
    selectedRating = val;
    document.querySelectorAll('#star-rating span').forEach((s, i) => s.classList.toggle('active', i < val));
}

function openReviewForm(name) {
    currentHeroForReview = name;
    selectedRating = 0;
    setRating(0);
    document.getElementById('rev-username').value = "";
    document.getElementById('rev-text').value = "";
    document.getElementById('review-title').innerText = `ОЦЕНКА ГЕРОЯ: ${name.toUpperCase()}`;

    document.querySelectorAll('.page').forEach(p => p.classList.add('hidden'));
    document.getElementById('review-form-section').classList.remove('hidden');
    window.scrollTo(0,0);
}

async function submitReview() {
    const username = document.getElementById('rev-username').value;
    const text = document.getElementById('rev-text').value;

    if (!username || !text || selectedRating === 0) {
        alert("Заполните поля и выберите рейтинг!");
        return;
    }

    await fetch(`${API_URL}/reviews`, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ username, hero_name: currentHeroForReview, text, rating: selectedRating })
    });
    navigateTo('reviews');
}

async function loadAllReviews() {
    try {
        const res = await fetch(`${API_URL}/reviews`);
        const data = await res.json();
        const container = document.getElementById('all-reviews-container');

        if (data.length === 0) {
            container.innerHTML = '<div class="no-reviews">Список отзывов пуст.</div>';
            return;
        }

        container.innerHTML = data.reverse().map(r => `
            <div class="review-card">
                <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                    <div>
                        <div style="color:var(--valve-yellow); margin-bottom: 8px; font-size: 18px;">${'★'.repeat(r.rating)}<span style="color:#222">${'★'.repeat(5-r.rating)}</span></div>
                        <div style="color: #fff; font-weight: 700; font-size: 22px;">${r.username}</div>
                        <div style="color: var(--dota-red); font-size: 11px; letter-spacing: 2px;">ГЕРОЙ: ${r.hero_name.toUpperCase()}</div>
                    </div>
                    <button class="table-action-btn" onclick="deleteReview(${r.id})">УДАЛИТЬ</button>
                </div>
                <div style="color: #888; font-family: 'Roboto Condensed'; font-size: 16px; margin-top: 15px; line-height: 1.6; font-style: italic;">
                    "${r.text}"
                </div>
            </div>
        `).join('');
    } catch (e) { console.error("Ошибка отзывов"); }
}

async function deleteReview(id) {
    if(confirm("Удалить отзыв?")) {
        await fetch(`${API_URL}/reviews/${id}`, { method: 'DELETE' });
        loadAllReviews();
    }
}

window.onload = () => navigateTo('home');