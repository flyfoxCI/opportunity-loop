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
/* Product DB: platform / visibility / grade buttons + search; items carry data-p, data-v, data-g, data-text. */
(function () {
  var bar = document.querySelector(".dbf");
  if (!bar) return;
  var sel = { p: "", v: "", g: "" }, q = bar.querySelector(".dbq"), n = bar.querySelector(".dbn");
  var items = document.querySelectorAll(".dbl > li[data-g]");
  function apply() {
    var t = (q && q.value || "").trim().toLowerCase(), shown = 0;
    items.forEach(function (li) {
      var ok = (!sel.p || (" " + li.dataset.p + " ").indexOf(" " + sel.p + " ") !== -1) &&
        (!sel.v || li.dataset.v === sel.v) && (!sel.g || li.dataset.g === sel.g) &&
        (!t || (li.dataset.text || "").indexOf(t) !== -1);
      li.classList.toggle("hidden", !ok);
      if (ok) shown++;
    });
    if (n) n.textContent = shown;
  }
  bar.addEventListener("click", function (ev) {
    var b = ev.target.closest("button[data-g]");
    if (!b) return;
    bar.querySelectorAll('button[data-g="' + b.dataset.g + '"]').forEach(function (x) { x.classList.toggle("on", x === b); });
    sel[b.dataset.g] = b.dataset.x;
    apply();
  });
  if (q) q.addEventListener("input", apply);
})();
