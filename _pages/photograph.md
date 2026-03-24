---
permalink: /photograph/
title: "Photograph"
layout: single
author_profile: false
---

<style>
.photograph-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.photograph-intro {
  text-align: center;
  margin-bottom: 40px;
  font-size: 1.1em;
  color: #666;
}

.photograph-year {
  margin-bottom: 40px;
}

.photograph-year h2 {
  border-bottom: 2px solid #ddd;
  padding-bottom: 10px;
  margin-bottom: 20px;
}

.photograph-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 20px;
}

.photograph-item {
  position: relative;
  overflow: hidden;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  cursor: pointer;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.photograph-item:hover {
  transform: translateY(-4px);
  box-shadow: 0 4px 16px rgba(0,0,0,0.15);
}

.photograph-item img {
  width: 100%;
  height: 250px;
  object-fit: cover;
  display: block;
}

/* Lightbox */
.lightbox {
  display: none;
  position: fixed;
  z-index: 9999;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0,0,0,0.9);
  justify-content: center;
  align-items: center;
  flex-direction: column;
}

.lightbox.active {
  display: flex;
}

.lightbox img {
  max-width: 90%;
  max-height: 80vh;
  object-fit: contain;
}

.lightbox-close {
  position: absolute;
  top: 20px;
  right: 30px;
  color: white;
  font-size: 40px;
  cursor: pointer;
  background: none;
  border: none;
}

.lightbox-nav {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  color: white;
  font-size: 30px;
  cursor: pointer;
  background: none;
  border: none;
  padding: 20px;
}

.lightbox-prev { left: 20px; }
.lightbox-next { right: 20px; }
</style>

<div class="photograph-container">
  <h1 class="entry-title" data-i18n="photograph-title">Photograph</h1>
  <p class="photograph-intro" data-i18n="photograph-desc">A collection of moments captured through my lens.</p>

  <div id="photo-grid"></div>
</div>

<div class="lightbox" id="lightbox">
  <button class="lightbox-close" onclick="closeLightbox()">&times;</button>
  <button class="lightbox-nav lightbox-prev" onclick="navigateLightbox(-1)">&#10094;</button>
  <img id="lightbox-img" src="" alt="">
  <button class="lightbox-nav lightbox-next" onclick="navigateLightbox(1)">&#10095;</button>
</div>

<script>
const photos = [
  { src: "/images/lxy/photograph/有迹可循.jpg", year: 2021 },
  { src: "/images/lxy/photograph/2 (9).jpg", year: 2021 },
  { src: "/images/lxy/photograph/3 (6).jpg", year: 2021 },
  { src: "/images/lxy/photograph/1 (37).jpg", year: 2021 },
  { src: "/images/lxy/photograph/3 (5).jpg", year: 2022 },
  { src: "/images/lxy/photograph/InterPhoto_1651233974871.jpg", year: 2022 },
  { src: "/images/lxy/photograph/2 (7).jpg", year: 2022 },
  { src: "/images/lxy/photograph/2 (1).jpg", year: 2022 },
  { src: "/images/lxy/photograph/1 (35).jpg", year: 2022 },
  { src: "/images/lxy/photograph/2 (16).jpg", year: 2022 },
  { src: "/images/lxy/photograph/1 (28).jpg", year: 2023 },
  { src: "/images/lxy/photograph/1 (13).jpg", year: 2023 },
  { src: "/images/lxy/photograph/1 (15).jpg", year: 2023 },
  { src: "/images/lxy/photograph/2 (2).jpg", year: 2023 },
  { src: "/images/lxy/photograph/2 (3).jpg", year: 2023 },
  { src: "/images/lxy/photograph/2 (5).jpg", year: 2023 },
  { src: "/images/lxy/photograph/1 (26).jpg", year: 2023 },
  { src: "/images/lxy/photograph/2 (18).jpg", year: 2023 },
  { src: "/images/lxy/photograph/1 (34).jpg", year: 2023 },
  { src: "/images/lxy/photograph/20231021-_DSC1304.jpg", year: 2023 }
];

let currentIndex = 0;

// Group photos by year
const photosByYear = {};
photos.forEach(photo => {
  if (!photosByYear[photo.year]) {
    photosByYear[photo.year] = [];
  }
  photosByYear[photo.year].push(photo);
});

// Render photos
function renderPhotos() {
  const grid = document.getElementById('photo-grid');
  const years = Object.keys(photosByYear).sort((a, b) => b - a);

  years.forEach(year => {
    const yearSection = document.createElement('div');
    yearSection.className = 'photograph-year';
    yearSection.innerHTML = `<h2>${year}</h2>`;

    const photoGrid = document.createElement('div');
    photoGrid.className = 'photograph-grid';

    photosByYear[year].forEach((photo, idx) => {
      const item = document.createElement('div');
      item.className = 'photograph-item';
      const globalIdx = photos.indexOf(photo);
      item.innerHTML = `<img src="${photo.src}" alt="Photo" onclick="openLightbox(${globalIdx})">`;
      photoGrid.appendChild(item);
    });

    yearSection.appendChild(photoGrid);
    grid.appendChild(yearSection);
  });
}

function openLightbox(index) {
  currentIndex = index;
  const lightbox = document.getElementById('lightbox');
  const img = document.getElementById('lightbox-img');
  img.src = photos[index].src;
  lightbox.classList.add('active');
  document.body.style.overflow = 'hidden';
}

function closeLightbox() {
  document.getElementById('lightbox').classList.remove('active');
  document.body.style.overflow = '';
}

function navigateLightbox(direction) {
  currentIndex = (currentIndex + direction + photos.length) % photos.length;
  document.getElementById('lightbox-img').src = photos[currentIndex].src;
}

// Keyboard navigation
document.addEventListener('keydown', (e) => {
  const lightbox = document.getElementById('lightbox');
  if (!lightbox.classList.contains('active')) return;

  if (e.key === 'Escape') closeLightbox();
  if (e.key === 'ArrowLeft') navigateLightbox(-1);
  if (e.key === 'ArrowRight') navigateLightbox(1);
});

// Close lightbox when clicking outside image
document.getElementById('lightbox').addEventListener('click', (e) => {
  if (e.target.id === 'lightbox') closeLightbox();
});

renderPhotos();
</script>
