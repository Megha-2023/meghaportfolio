document.addEventListener('DOMContentLoaded', function() {
  const toggle = document.getElementById('lang-toggle');
  const languageInput = document.getElementById('language-input');
  const form = document.getElementById('lang-form');

  if (toggle && languageInput && form) {
    toggle.addEventListener('change', function() {
      languageInput.value = this.checked ? 'fr' : 'en';
      form.submit();
      setTimeout(() => {
        window.location.reload();
      }, 500);
    });
  }
});