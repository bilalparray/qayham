const cards = document.querySelectorAll(".testimonial-card");
const navButtons = document.querySelectorAll(".testimonial-nav-btn");
let currentIndex = 0;
let autoSlide;

function showCard(index) {
  cards.forEach((card) => card.classList.remove("active"));
  navButtons.forEach((btn) => btn.classList.remove("active"));

  cards[index].classList.add("active");
  navButtons[index].classList.add("active");
  currentIndex = index;
}

navButtons.forEach((btn, index) => {
  btn.addEventListener("click", () => {
    clearInterval(autoSlide); // pause auto-slide when clicked
    showCard(index);
    startAutoSlide(); // restart auto-slide
  });
});

function startAutoSlide() {
  autoSlide = setInterval(() => {
    const nextIndex = (currentIndex + 1) % cards.length;
    showCard(nextIndex);
  }, 5000); // change every 5 seconds
}

// Init
showCard(currentIndex);
startAutoSlide();

const backToTopBtn = document.getElementById("backToTop");

// Show or hide the button on scroll
window.addEventListener("scroll", () => {
  if (window.scrollY > 300) {
    backToTopBtn.classList.add("show");
  } else {
    backToTopBtn.classList.remove("show");
  }
});

// Scroll to top on click
backToTopBtn.addEventListener("click", () => {
  window.scrollTo({
    top: 0,
    behavior: "smooth",
  });
});
