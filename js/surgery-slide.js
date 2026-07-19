/**
 * Surgery Slide — Shared scaling & functionality
 * All surgery presentations use this for consistent responsive behavior
 */
(function() {
  'use strict';

  function scaleSlide() {
    var s = document.querySelector('.slide-content');
    if (!s) return;
    var sx = window.innerWidth / 960;
    var sy = window.innerHeight / 540;
    var sc = Math.min(sx, sy);
    s.style.width = '960px';
    s.style.height = '540px';
    s.style.transform = 'scale(' + sc + ')';
    s.style.transformOrigin = 'center center';
    s.style.flexShrink = '0';
  }

  function init() {
    scaleSlide();
    window.addEventListener('resize', scaleSlide);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
