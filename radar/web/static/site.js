/* Opportunity Loop v3: surface tabs, text filter, theme toggle. The page works without it. */
function olTheme() {
  var root = document.documentElement;
  var dark = root.dataset.theme ? root.dataset.theme === "dark"
    : window.matchMedia("(prefers-color-scheme: dark)").matches;
  root.dataset.theme = dark ? "light" : "dark";
  try { localStorage.setItem("ol-theme", root.dataset.theme); } catch (e) {}
}
(function () {
  var tabs = document.querySelectorAll(".tab[data-f]");
  var search = document.querySelector(".search");
  if (!tabs.length && !search) return;
  var surface = "all";
  function apply() {
    var q = (search && search.value || "").trim().toLowerCase();
    document.querySelectorAll("[data-surface]").forEach(function (el) {
      var okS = surface === "all" || el.dataset.surface === surface;
      var okQ = !q || (el.dataset.text || "").indexOf(q) !== -1;
      el.classList.toggle("hidden", !(okS && okQ));
    });
  }
  tabs.forEach(function (t) {
    t.addEventListener("click", function () {
      tabs.forEach(function (x) { x.classList.remove("on"); });
      t.classList.add("on");
      surface = t.dataset.f;
      try { sessionStorage.setItem("ol-tab", surface); } catch (e) {}
      apply();
    });
  });
  if (search) search.addEventListener("input", apply);
  try {
    var saved = sessionStorage.getItem("ol-tab");
    if (saved) { var b = document.querySelector('.tab[data-f="' + saved + '"]'); if (b) b.click(); }
  } catch (e) {}
})();
