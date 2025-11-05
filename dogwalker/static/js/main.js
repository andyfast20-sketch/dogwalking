const navToggle = document.querySelector(".nav-toggle");
const primaryNav = document.querySelector(".primary-nav");

if (navToggle && primaryNav) {
  navToggle.addEventListener("click", () => {
    const isExpanded = navToggle.getAttribute("aria-expanded") === "true";
    navToggle.setAttribute("aria-expanded", String(!isExpanded));
    primaryNav.classList.toggle("open");
  });
}

const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("reveal");
      }
    });
  },
  {
    rootMargin: "-10% 0px",
    threshold: 0.1,
  }
);

document
  .querySelectorAll(
    ".highlight-card, .service-card, .testimonial-card, .team-card, .recent-bookings li, .cta-inner, .booking-copy, .booking-form"
  )
  .forEach((section) => {
    observer.observe(section);
  });
