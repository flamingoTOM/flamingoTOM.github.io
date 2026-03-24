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
  font-family: "Times New Roman", "Cambria Math", serif;
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
  font-family: "Times New Roman", "Cambria Math", serif;
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

  <div class="photograph-year">
    <h2>2023</h2>
    <div class="photograph-grid">
      <div class="photograph-item"><img src="/images/lxy/photograph/1 (13).jpg" alt="Photo" onclick="openLightbox(0)"></div>
      <div class="photograph-item"><img src="/images/lxy/photograph/1 (15).jpg" alt="Photo" onclick="openLightbox(1)"></div>
      <div class="photograph-item"><img src="/images/lxy/photograph/1 (26).jpg" alt="Photo" onclick="openLightbox(2)"></div>
      <div class="photograph-item"><img src="/images/lxy/photograph/1 (28).jpg" alt="Photo" onclick="openLightbox(3)"></div>
      <div class="photograph-item"><img src="/images/lxy/photograph/1 (34).jpg" alt="Photo" onclick="openLightbox(4)"></div>
      <div class="photograph-item"><img src="/images/lxy/photograph/2 (2).jpg" alt="Photo" onclick="openLightbox(5)"></div>
      <div class="photograph-item"><img src="/images/lxy/photograph/2 (3).jpg" alt="Photo" onclick="openLightbox(6)"></div>
      <div class="photograph-item"><img src="/images/lxy/photograph/2 (5).jpg" alt="Photo" onclick="openLightbox(7)"></div>
      <div class="photograph-item"><img src="/images/lxy/photograph/2 (18).jpg" alt="Photo" onclick="openLightbox(8)"></div>
      <div class="photograph-item"><img src="/images/lxy/photograph/20231021-_DSC1304.jpg" alt="Photo" onclick="openLightbox(9)"></div>
    </div>
  </div>

  <div class="photograph-year">
    <h2>2022</h2>
    <div class="photograph-grid">
      <div class="photograph-item"><img src="/images/lxy/photograph/1 (35).jpg" alt="Photo" onclick="openLightbox(10)"></div>
      <div class="photograph-item"><img src="/images/lxy/photograph/2 (1).jpg" alt="Photo" onclick="openLightbox(11)"></div>
      <div class="photograph-item"><img src="/images/lxy/photograph/2 (7).jpg" alt="Photo" onclick="openLightbox(12)"></div>
      <div class="photograph-item"><img src="/images/lxy/photograph/2 (16).jpg" alt="Photo" onclick="openLightbox(13)"></div>
      <div class="photograph-item"><img src="/images/lxy/photograph/3 (5).jpg" alt="Photo" onclick="openLightbox(14)"></div>
      <div class="photograph-item"><img src="/images/lxy/photograph/InterPhoto_1651233974871.jpg" alt="Photo" onclick="openLightbox(15)"></div>
    </div>
  </div>

  <div class="photograph-year">
    <h2>2021</h2>
    <div class="photograph-grid">
      <div class="photograph-item"><img src="/images/lxy/photograph/1 (37).jpg" alt="Photo" onclick="openLightbox(16)"></div>
      <div class="photograph-item"><img src="/images/lxy/photograph/2 (9).jpg" alt="Photo" onclick="openLightbox(17)"></div>
      <div class="photograph-item"><img src="/images/lxy/photograph/3 (6).jpg" alt="Photo" onclick="openLightbox(18)"></div>
      <div class="photograph-item"><img src="/images/lxy/photograph/有迹可循.jpg" alt="Photo" onclick="openLightbox(19)"></div>
    </div>
  </div>
</div>

<div class="lightbox" id="lightbox">
  <button class="lightbox-close" onclick="closeLightbox()">&times;</button>
  <button class="lightbox-nav lightbox-prev" onclick="navigateLightbox(-1)">&#10094;</button>
  <img id="lightbox-img" src="" alt="">
  <button class="lightbox-nav lightbox-next" onclick="navigateLightbox(1)">&#10095;</button>
</div>

<script>
var photos = [
  "/images/lxy/photograph/1 (13).jpg",
  "/images/lxy/photograph/1 (15).jpg",
  "/images/lxy/photograph/1 (26).jpg",
  "/images/lxy/photograph/1 (28).jpg",
  "/images/lxy/photograph/1 (34).jpg",
  "/images/lxy/photograph/2 (2).jpg",
  "/images/lxy/photograph/2 (3).jpg",
  "/images/lxy/photograph/2 (5).jpg",
  "/images/lxy/photograph/2 (18).jpg",
  "/images/lxy/photograph/20231021-_DSC1304.jpg",
  "/images/lxy/photograph/1 (35).jpg",
  "/images/lxy/photograph/2 (1).jpg",
  "/images/lxy/photograph/2 (7).jpg",
  "/images/lxy/photograph/2 (16).jpg",
  "/images/lxy/photograph/3 (5).jpg",
  "/images/lxy/photograph/InterPhoto_1651233974871.jpg",
  "/images/lxy/photograph/1 (37).jpg",
  "/images/lxy/photograph/2 (9).jpg",
  "/images/lxy/photograph/3 (6).jpg",
  "/images/lxy/photograph/有迹可循.jpg"
];

var currentIndex = 0;

function openLightbox(index) {
  currentIndex = index;
  var lightbox = document.getElementById('lightbox');
  var img = document.getElementById('lightbox-img');
  img.src = photos[index];
  lightbox.classList.add('active');
  document.body.style.overflow = 'hidden';
}

function closeLightbox() {
  document.getElementById('lightbox').classList.remove('active');
  document.body.style.overflow = '';
}

function navigateLightbox(direction) {
  currentIndex = (currentIndex + direction + photos.length) % photos.length;
  document.getElementById('lightbox-img').src = photos[currentIndex];
}

document.addEventListener('keydown', function(e) {
  var lightbox = document.getElementById('lightbox');
  if (!lightbox.classList.contains('active')) return;
  if (e.key === 'Escape') closeLightbox();
  if (e.key === 'ArrowLeft') navigateLightbox(-1);
  if (e.key === 'ArrowRight') navigateLightbox(1);
});

document.getElementById('lightbox').addEventListener('click', function(e) {
  if (e.target.id === 'lightbox') closeLightbox();
});
</script>
