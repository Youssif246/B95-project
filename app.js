/**
 * B95 PROJECT — Clean Monograph Interactions
 * Minimal navigation active state and print routing
 */

const initializePage = () => {
  const navLinks = document.querySelectorAll('.nav-links-group a');
  const navMenu = document.querySelector('.nav-menu');
  const sections = document.querySelectorAll('section.page-spread[id]');

  navLinks.forEach(link => {
    link.addEventListener('click', () => {
      navMenu.open = false;
    });
  });

  document.addEventListener('click', event => {
    if (navMenu.open && !navMenu.contains(event.target)) navMenu.open = false;
  });

  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && navMenu.open) {
      navMenu.open = false;
      navMenu.querySelector('summary').focus();
    }
  });

  window.addEventListener('resize', () => {
    if (window.innerWidth > 860) navMenu.open = false;
  });

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
};

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initializePage, { once: true });
} else {
  initializePage();
}
