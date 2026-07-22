
function toggleDept(header) {
  const body = header.nextElementSibling;
  const isOpen = body.classList.contains('open');
  document.querySelectorAll('.dept-body').forEach(b => b.classList.remove('open'));
  document.querySelectorAll('.dept-header').forEach(h => h.classList.remove('open'));
  if (!isOpen) { body.classList.add('open'); header.classList.add('open'); }
}

function runReveal() {
  const els = document.querySelectorAll('.reveal, .reveal-left, .reveal-right, .stagger');
  els.forEach(el => {
    const rect = el.getBoundingClientRect();
    if (rect.top < window.innerHeight - 60) el.classList.add('visible');
  });
}

window.addEventListener('scroll', runReveal, { passive: true });
setTimeout(runReveal, 120);

// ── HAMBURGER NAV TOGGLE ──
(function () {
  const toggle   = document.getElementById('navToggle');
  const nav      = document.querySelector('header nav');
  const backdrop = document.getElementById('navBackdrop');
  if (!toggle || !nav) return;

  function openNav() {
    nav.classList.add('open');
    backdrop && backdrop.classList.add('open');
    document.body.style.overflow = 'hidden';
    toggle.querySelector('i').className = 'ti ti-x';
  }
  function closeNav() {
    nav.classList.remove('open');
    backdrop && backdrop.classList.remove('open');
    document.body.style.overflow = '';
    toggle.querySelector('i').className = 'ti ti-menu-2';
  }

  toggle.addEventListener('click', () =>
    nav.classList.contains('open') ? closeNav() : openNav()
  );
  backdrop && backdrop.addEventListener('click', closeNav);
  nav.querySelectorAll('a').forEach(a => a.addEventListener('click', closeNav));
})();

// ── COUNSELLING FORM ──
(function () {
  const form = document.getElementById('counsellingForm');
  if (!form) return;

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    const name    = document.getElementById('c-name').value.trim();
    const phone   = document.getElementById('c-phone').value.trim();
    const type    = document.getElementById('c-type').value;
    const desc    = document.getElementById('c-desc').value.trim();
    const contact = document.getElementById('c-contact').value;
    const time    = document.getElementById('c-time').value;
    const errEl   = document.getElementById('form-error');

    if (!name || !phone || !type) {
      errEl.textContent = 'Please fill in your name, phone number, and type of counselling.';
      errEl.style.display = 'block';
      return;
    }
    errEl.style.display = 'none';

    const message = [
      '🙏 *Counselling Request – JCK Church*',
      '-----------------------------------',
      '*Name:* ' + name,
      '*Phone:* ' + phone,
      '*Type:* ' + type,
      desc ? '*Details:* ' + desc : null,
      '*Contact via:* ' + contact,
      '*Best time:* ' + time,
    ].filter(Boolean).join('\n');

    window.open('https://wa.me/27693907152?text=' + encodeURIComponent(message), '_blank');
  });
})();
