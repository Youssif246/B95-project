/**
 * B95 PROJECT — Clean Monograph Interactions
 * Minimal navigation active state and print routing
 */

document.addEventListener('DOMContentLoaded', () => {
  const navLinks = document.querySelectorAll('.nav-links-group a');
  const sections = document.querySelectorAll('section.profile-sheet');

  // Simple active state observer
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const id = entry.target.id;
        navLinks.forEach(link => {
          const href = link.getAttribute('href').replace('#', '');
          if (href === id) {
            link.classList.add('active');
          } else {
            link.classList.remove('active');
          }
        });
      }
    });
  }, {
    rootMargin: '-20% 0px -60% 0px',
    threshold: 0
  });

  sections.forEach(sec => observer.observe(sec));
});
