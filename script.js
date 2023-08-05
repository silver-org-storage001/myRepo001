// Function to animate the card using GSAP
function animateCard() {
  // Elements to animate
  const greeting = document.querySelector('.greeting');
  const message = document.querySelector('.message');
  const loveBtn = document.querySelector('.love-btn');
  const heartsContainer = document.querySelector('.heart-container');

  // Create the animation timeline
  const tl = gsap.timeline();

  // Animate the elements
  tl.from(greeting, { opacity: 0, y: -50, duration: 1 });
  tl.from(message, { opacity: 0, y: 50, duration: 1 });
  tl.from(loveBtn, { opacity: 0, scale: 0.5, duration: 0.5 });

  // Generate and animate raining hearts
  const heartCount = 30;
  const hearts = [];

  for (let i = 0; i < heartCount; i++) {
    const heart = document.createElement('div');
    heart.className = 'heart';
    heart.style.left = `${Math.random() * 100}%`;
    heart.style.animationDuration = `${1 + Math.random() * 2}s`;
    heart.style.animationDelay = `${Math.random() * 2}s`;
    heartsContainer.appendChild(heart);
    hearts.push(heart);
  }

  tl.from(hearts, { y: -100, opacity: 50, stagger: 0.2, ease: 'back.out(1.7)', duration: 2 });
}

// Call the animateCard function when the page has loaded
window.onload = function () {
  animateCard();
};
