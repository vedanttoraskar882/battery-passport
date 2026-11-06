/**
 * Battery Passport Network — Application Scripts
 * Manages routing, deep linking, interactive states, animations, and Chart.js telemetry.
 */

// Global Chart tracking
window._chartsInitialized = false;

/**
 * Route switcher between pages
 * @param {string} pageId - e.g. 'home', 'about', 'platform', etc.
 */
function showPage(pageId) {
  // Update pages
  const pages = document.querySelectorAll('.page');
  pages.forEach(p => p.classList.remove('active'));

  // Update nav buttons
  const navBtns = document.querySelectorAll('.nav-links button');
  navBtns.forEach(b => b.classList.remove('active'));

  const targetPage = document.getElementById('page-' + pageId);
  if (targetPage) {
    targetPage.classList.add('active');
  }

  const targetBtn = document.getElementById('nav-' + pageId);
  if (targetBtn) {
    targetBtn.classList.add('active');
  }

  // Instant scroll to top on route change
  window.scrollTo({ top: 0, behavior: 'instant' });

  // Initialize charts on market page visit
  if (pageId === 'market' && !window._chartsInitialized) {
    initCharts();
    window._chartsInitialized = true;
  }
}

/**
 * Navigate to a specific page and smoothly scroll to target anchor
 * @param {string} pageId - Target page
 * @param {string} anchorId - Target element ID
 */
function goSection(pageId, anchorId) {
  showPage(pageId);
  setTimeout(function() {
    const el = document.getElementById(anchorId);
    if (el) {
      el.scrollIntoView({ behavior: 'smooth', block: 'start' });
      el.classList.add('deep-link-flash');
      setTimeout(() => el.classList.remove('deep-link-flash'), 1600);
    }
  }, 60);
}

/**
 * Toggle expandable platform capability card
 * @param {HTMLElement} btn - The clicked button
 */
function toggleCard(btn) {
  const card = btn.closest('.plat-card');
  if (card) {
    card.classList.toggle('open');
    btn.innerHTML = card.classList.contains('open') ? 'Show Less' : 'Learn More';
  }
}

/**
 * Toggle FAQ accordion item
 * @param {HTMLElement} el - The clicked FAQ element or its parent
 */
function toggleFAQ(el) {
  if (el) {
    el.classList.toggle('open');
  }
}

/**
 * Close mobile navigation drawer
 */
function closeMob() {
  const mobNav = document.getElementById('mobileNav');
  const burger = document.getElementById('hamburger');
  if (mobNav) mobNav.classList.remove('open');
  if (burger) burger.classList.remove('open');
}

// Mobile Hamburger Toggle Listener
document.addEventListener('DOMContentLoaded', function() {
  const burger = document.getElementById('hamburger');
  const mobNav = document.getElementById('mobileNav');
  if (burger && mobNav) {
    burger.addEventListener('click', function() {
      this.classList.toggle('open');
      mobNav.classList.toggle('open');
    });
  }

  // IntersectionObserver to pause hero circuit pulse when hero is offscreen
  const heroElement = document.querySelector('.hero');
  const circuitElement = document.querySelector('.hero-circuits');
  if (heroElement && circuitElement && 'IntersectionObserver' in window) {
    const heroObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          circuitElement.classList.remove('animation-paused');
        } else {
          circuitElement.classList.add('animation-paused');
        }
      });
    }, { threshold: 0.05 });
    heroObserver.observe(heroElement);
  }
});

/**
 * Handle Contact Form submission
 * @param {Event} e - Submit event
 */
function handleSubmit(e) {
  e.preventDefault();
  const form = e.target;
  const submitBtn = form.querySelector('button[type="submit"]');
  if (!submitBtn) return;

  const originalHtml = submitBtn.innerHTML;
  submitBtn.innerHTML = '<i class="fas fa-check"></i> Demo Request Sent!';
  submitBtn.style.background = 'linear-gradient(135deg, #14D97D, #2E8FE0)';
  submitBtn.style.color = '#080D0B';
  submitBtn.disabled = true;

  setTimeout(() => {
    submitBtn.innerHTML = 'Send Demo Request <i class="fas fa-arrow-right" style="margin-left:6px"></i>';
    submitBtn.style.background = '';
    submitBtn.style.color = '';
    submitBtn.disabled = false;
    form.reset();
  }, 3500);
}

/**
 * Initialize Chart.js telemetry models on Market Analysis page
 */
function initCharts() {
  if (typeof Chart === 'undefined') return;

  const B = 'rgba(20, 217, 125, 0.85)';
  const B2 = 'rgba(20, 217, 125, 0.4)';
  const A = 'rgba(46, 143, 224, 0.85)';
  const A2 = 'rgba(46, 143, 224, 0.45)';
  const G = 'rgba(60, 242, 196, 0.8)';
  const GR = 'rgba(13, 20, 17, 0.08)';
  const MT = 'rgba(44, 62, 55, 0.85)';

  Chart.defaults.font.family = "'IBM Plex Mono', monospace";
  Chart.defaults.font.size = 11;
  Chart.defaults.color = MT;

  // Chart 1: Top Operational Pain Points
  const chartSectorEl = document.getElementById('chartSector');
  if (chartSectorEl) {
    new Chart(chartSectorEl, {
      type: 'bar',
      data: {
        labels: [
          'Unverified/Counterfeit Replacements',
          'Miscalculated Residual Life',
          'High Post-Sale Return Rate',
          'Lack of Structured BPN Taxonomy',
          'Inconsistent Manual Grading'
        ],
        datasets: [{
          label: '%',
          data: [28.2, 32, 22.6, 17.5, 11.3],
          backgroundColor: [B, A, B2, G, A2],
          borderRadius: 6,
          barPercentage: 0.6
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: { display: false }
        },
        scales: {
          x: {
            grid: { display: false },
            ticks: {
              maxRotation: 55,
              minRotation: 0,
              autoSkip: false,
              font: { size: window.innerWidth < 480 ? 8 : 9 }
            }
          },
          y: {
            grid: { color: GR },
            ticks: { callback: v => v + '%' }
          }
        }
      }
    });
  }

  // Chart 2: Modelled Feature Demand
  const chartRootCauseEl = document.getElementById('chartRootCause');
  if (chartRootCauseEl) {
    new Chart(chartRootCauseEl, {
      type: 'doughnut',
      data: {
        labels: [
          'Predictive Residual Life (91%)',
          'Automated BPN Classification (89%)',
          'Replacement Authenticity Forensics (83%)',
          'Compliance Reporting (85%)',
          'Federated Benchmarking (80%)'
        ],
        datasets: [{
          data: [91, 89, 83, 85, 80],
          backgroundColor: [B, A, G, B2, A2],
          borderWidth: 1.5,
          borderColor: '#FFFFFF'
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            position: 'bottom',
            labels: { boxWidth: 10, padding: 8, font: { size: 9 } }
          }
        }
      }
    });
  }

  // Chart 3: Battery Passport Network vs. Competing Approaches
  const chartRadarEl = document.getElementById('chartRadar');
  if (chartRadarEl) {
    new Chart(chartRadarEl, {
      type: 'radar',
      data: {
        labels: [
          'Closed-Loop Outcome',
          'Replacement Authenticity',
          'UK SME Benchmarking',
          'DNA Fingerprinting',
          'Residual Life Prediction',
          'Ease of SME Adoption'
        ],
        datasets: [
          {
            label: 'Battery Passport Network',
            data: [5, 5, 5, 5, 5, 5],
            backgroundColor: 'rgba(20, 217, 125, 0.12)',
            borderColor: B,
            borderWidth: 2,
            pointBackgroundColor: B
          },
          {
            label: 'Blancco / PhoneCheck',
            data: [1, 1, 1, 2, 1, 2],
            backgroundColor: 'rgba(46, 143, 224, 0.05)',
            borderColor: A2,
            borderWidth: 1.5,
            pointBackgroundColor: A2
          },
          {
            label: 'Back Market / OEM Screens',
            data: [1, 1, 1, 1, 1, 3],
            backgroundColor: 'rgba(13, 20, 17, 0.04)',
            borderColor: 'rgba(13, 20, 17, 0.4)',
            borderWidth: 1.5,
            pointBackgroundColor: 'rgba(13, 20, 17, 0.4)'
          },
          {
            label: 'EV Passports / GBA',
            data: [1, 1, 1, 1, 1, 1],
            backgroundColor: 'rgba(60, 242, 196, 0.06)',
            borderColor: 'rgba(60, 242, 196, 0.6)',
            borderWidth: 1.5,
            pointBackgroundColor: 'rgba(60, 242, 196, 0.6)'
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            position: 'bottom',
            labels: { boxWidth: 10, padding: 10, font: { size: 9 } }
          }
        },
        scales: {
          r: {
            grid: { color: GR },
            pointLabels: { font: { size: 10 } },
            ticks: { display: false },
            min: 0,
            max: 5
          }
        }
      }
    });
  }

  // Chart 4: UK E-Waste & Refurbishment Market Growth
  const chartGrowthEl = document.getElementById('chartGrowth');
  if (chartGrowthEl) {
    new Chart(chartGrowthEl, {
      type: 'bar',
      data: {
        labels: ['2024', '2026', '2028', '2029', '2031', '2033', '2035'],
        datasets: [
          {
            label: 'UK E-Waste & Refurb Market ($B)',
            data: [1.49, 1.94, 2.53, 2.89, 3.77, 4.92, 6.42],
            backgroundColor: A,
            borderRadius: 5,
            barPercentage: 0.55
          },
          {
            type: 'line',
            label: 'CAGR %',
            data: [null, 14.2, 14.2, 14.2, 14.2, 14.2, 14.2],
            borderColor: B,
            borderWidth: 2,
            yAxisID: 'y2',
            tension: 0.4,
            pointBackgroundColor: B,
            fill: false
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            position: 'bottom',
            labels: {
              boxWidth: 10,
              padding: 8,
              font: { size: window.innerWidth < 480 ? 8 : 10 }
            }
          }
        },
        scales: {
          x: {
            grid: { color: GR },
            ticks: { font: { size: window.innerWidth < 480 ? 8 : 10 } }
          },
          y: {
            grid: { color: GR },
            ticks: {
              callback: v => '$' + v + 'B',
              font: { size: window.innerWidth < 480 ? 8 : 10 }
            }
          },
          y2: {
            position: 'right',
            grid: { display: false },
            ticks: {
              callback: v => v + '%',
              font: { size: window.innerWidth < 480 ? 8 : 10 }
            }
          }
        }
      }
    });
  }
}
