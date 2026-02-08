// Application Slideshow Hero
(function() {
  let currentSlide = 0;
  let slides = [];
  let indicators = [];
  let autoPlayInterval = null;
  const AUTOPLAY_DELAY = 5000; // 5 seconds

  // Initialize slideshow when DOM is ready
  function initSlideshow() {
    slides = document.querySelectorAll('.slide');
    indicators = document.querySelectorAll('.indicator');

    if (slides.length === 0) return;

    // Start autoplay
    startAutoPlay();

    // Pause autoplay on hover
    const slideshowContainer = document.querySelector('.slideshow-container');
    if (slideshowContainer) {
      slideshowContainer.addEventListener('mouseenter', stopAutoPlay);
      slideshowContainer.addEventListener('mouseleave', startAutoPlay);
    }
  }

  // Show specific slide
  function showSlide(index) {
    // Wrap around if index is out of bounds
    if (index >= slides.length) {
      currentSlide = 0;
    } else if (index < 0) {
      currentSlide = slides.length - 1;
    } else {
      currentSlide = index;
    }

    // Update slides
    slides.forEach((slide, i) => {
      if (i === currentSlide) {
        slide.classList.add('active');
      } else {
        slide.classList.remove('active');
      }
    });

    // Update indicators
    indicators.forEach((indicator, i) => {
      if (i === currentSlide) {
        indicator.classList.add('active');
      } else {
        indicator.classList.remove('active');
      }
    });
  }

  // Change slide by offset
  window.changeSlide = function(offset) {
    stopAutoPlay();
    showSlide(currentSlide + offset);
    startAutoPlay();
  };

  // Go to specific slide
  window.goToSlide = function(index) {
    stopAutoPlay();
    showSlide(index);
    startAutoPlay();
  };

  // Auto-play functions
  function startAutoPlay() {
    stopAutoPlay(); // Clear any existing interval
    autoPlayInterval = setInterval(() => {
      showSlide(currentSlide + 1);
    }, AUTOPLAY_DELAY);
  }

  function stopAutoPlay() {
    if (autoPlayInterval) {
      clearInterval(autoPlayInterval);
      autoPlayInterval = null;
    }
  }

  // Initialize on DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initSlideshow);
  } else {
    initSlideshow();
  }

  // Re-initialize when language changes (to ensure proper text display)
  window.addEventListener('languageChanged', () => {
    // Slideshow structure doesn't change, just text content via i18n
    // No need to re-initialize, i18n system handles text updates
  });
})();
