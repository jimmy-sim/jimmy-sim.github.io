// Compatibility for project links shared before articles moved into projects/.
(() => {
  const target = new URL(document.currentScript.dataset.target, document.baseURI);
  target.search = window.location.search;
  target.hash = window.location.hash;
  window.location.replace(target.href);
})();
