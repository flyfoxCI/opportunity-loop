(function () {
  "use strict";
  var store = {
    get: function (k, d) { try { var v = localStorage.getItem(k); return v ? JSON.parse(v) : d; } catch (e) { return d; } },
    set: function (k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) {} }
  };

  // ---- theme
  var t = store.get("radar-theme", null);
  if (t) document.documentElement.setAttribute("data-theme", t);
  document.querySelectorAll("[data-theme-toggle]").forEach(function (b) {
    b.addEventListener("click", function () {
      var cur = document.documentElement.getAttribute("data-theme") ||
        (matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
      var next = cur === "dark" ? "light" : "dark";
      document.documentElement.setAttribute("data-theme", next);
      store.set("radar-theme", next);
    });
  });

  // ---- filter chips: <div class="filters" data-filter-for="#grid"> buttons with data-v; items have data-f
  document.querySelectorAll(".filters[data-filter-for]").forEach(function (bar) {
    var grid = document.querySelector(bar.getAttribute("data-filter-for"));
    bar.addEventListener("click", function (e) {
      var b = e.target.closest("button"); if (!b) return;
      bar.querySelectorAll("button").forEach(function (x) { x.classList.toggle("on", x === b); });
      var v = b.getAttribute("data-v");
      grid.querySelectorAll("[data-f]").forEach(function (it) {
        it.style.display = (v === "all" || (" " + it.getAttribute("data-f") + " ").indexOf(" " + v + " ") >= 0) ? "" : "none";
      });
    });
  });

  // ---- sortable tables
  document.querySelectorAll("table[data-sortable]").forEach(function (tbl) {
    tbl.querySelectorAll("th.sortable").forEach(function (th, i) {
      var idx = Array.prototype.indexOf.call(th.parentNode.children, th), asc = false;
      th.addEventListener("click", function () {
        asc = !asc;
        var body = tbl.tBodies[0], rows = Array.prototype.slice.call(body.rows);
        rows.sort(function (a, b) {
          var x = a.cells[idx].getAttribute("data-s") || a.cells[idx].textContent,
              y = b.cells[idx].getAttribute("data-s") || b.cells[idx].textContent;
          var nx = parseFloat(x), ny = parseFloat(y);
          var r = (!isNaN(nx) && !isNaN(ny)) ? nx - ny : String(x).localeCompare(String(y));
          return asc ? r : -r;
        });
        rows.forEach(function (r) { body.appendChild(r); });
      });
    });
  });

  // ---- watch directions (per-viewer, browser only)
  var watched = store.get("radar-watch", []);
  document.querySelectorAll("[data-watch]").forEach(function (b) {
    var slug = b.getAttribute("data-watch");
    function paint() { var on = watched.indexOf(slug) >= 0; b.classList.toggle("on", on); b.textContent = on ? "Watching (saved in this browser)" : "Watch this direction"; }
    paint();
    b.addEventListener("click", function () {
      var i = watched.indexOf(slug);
      if (i >= 0) watched.splice(i, 1); else watched.push(slug);
      store.set("radar-watch", watched); paint();
    });
  });
  var mine = document.getElementById("watching");
  if (mine) {
    var cards = Array.prototype.slice.call(document.querySelectorAll("#all-dir-rows [data-slug]"));
    var hits = cards.filter(function (c) { return watched.indexOf(c.getAttribute("data-slug")) >= 0; });
    if (hits.length) {
      mine.hidden = false;
      var g = mine.querySelector(".rank");
      hits.forEach(function (c) { g.appendChild(c.cloneNode(true)); });
    }
  }

  // ---- idea checker
  var form = document.getElementById("check-form");
  if (form) initCheck(form);

  function tokens(s) {
    var stop = "a an the and or for to of in on with my your our app tool that which who is are be it this into from by at as ai saas platform software help helps people users".split(" ");
    return (s.toLowerCase().match(/[a-z0-9][a-z0-9\-]+/g) || []).filter(function (w) { return w.length > 2 && stop.indexOf(w) < 0; });
  }
  function esc(s) { return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); }
  function money(v) { if (!v) return "–"; if (v >= 1e6) return "$" + (v / 1e6).toFixed(1) + "M"; if (v >= 1e4) return "$" + Math.round(v / 1e3) + "K"; if (v >= 1e3) return "$" + (v / 1e3).toFixed(1) + "K"; return "$" + Math.round(v); }

  function initCheck(form) {
    var data = null, out = document.getElementById("check-out");
    fetch(form.getAttribute("data-src")).then(function (r) { return r.json(); }).then(function (d) { data = d; form.querySelector("button").disabled = false; })
      .catch(function () { out.innerHTML = '<p class="empty">Could not load radar data.</p>'; });
    var draft = store.get("radar-check-draft", "");
    if (draft) form.idea.value = draft;
    form.idea.addEventListener("input", function () { store.set("radar-check-draft", form.idea.value); });
    form.querySelectorAll("[data-example]").forEach(function (b) {
      b.addEventListener("click", function () {
        form.idea.value = b.getAttribute("data-example");
        store.set("radar-check-draft", form.idea.value);
        if (form.requestSubmit) form.requestSubmit(); else form.querySelector("button[type=submit]").click();
      });
    });

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!data) return;
      var idea = form.idea.value.trim(); if (!idea) return;
      var toks = tokens(idea), low = " " + idea.toLowerCase() + " ";
      // rank directions by keyword hits
      var ranked = data.directions.map(function (d) {
        var s = 0;
        d.keywords.forEach(function (k) { if (low.indexOf(" " + k.trim()) >= 0 || low.indexOf(k.trim()) >= 0 && k.length > 4) s += 2; });
        toks.forEach(function (w) { d.keywords.forEach(function (k) { if (k.indexOf(w) === 0 || w.indexOf(k.trim()) === 0) s += 1; }); if (d.name.toLowerCase().indexOf(w) >= 0) s += 1; });
        return { d: d, s: s };
      }).filter(function (x) { return x.s > 0; }).sort(function (a, b) { return b.s - a.s; }).slice(0, 3);
      // comparables by token overlap
      var comps = data.products.map(function (p) {
        var text = (p.name + " " + p.desc).toLowerCase(), s = 0;
        toks.forEach(function (w) { if (text.indexOf(w) >= 0) s += 1; });
        return { p: p, s: s };
      }).filter(function (x) { return x.s >= Math.min(2, toks.length); })
        .sort(function (a, b) { return b.s - a.s || (b.p.mrr || 0) - (a.p.mrr || 0); }).slice(0, 10);

      var top = ranked[0] && ranked[0].d;
      var subs = top ? top.subreddits.slice() : ["SaaS", "Entrepreneur", "smallbusiness"];
      var q = toks.slice(0, 3).join(" ");
      render(idea, ranked, comps, top, subs, q, null);
      reddit(subs, q, function (res) { render(idea, ranked, comps, top, subs, q, res); });
    });

    // Arctic Shift full-text search times out on big subreddits, so pull the newest posts
    // (2 pages per subreddit) and match the idea's words locally.
    function reddit(subs, q, cb) {
      var words = q.split(/\s+/).filter(Boolean), all = [], left = subs.length, errs = 0;
      var intent = /\b(looking for|recommend|alternative|is there (an?|any)|what do you use|best (app|tool)|would pay|tired of|too expensive|need (an? )?(app|tool|way))/i;
      function page(sub, before, n, done) {
        var u = "https://arctic-shift.photon-reddit.com/api/posts/search?subreddit=" + encodeURIComponent(sub) +
          "&limit=100&sort=desc&fields=id,title,selftext,num_comments,score,subreddit,author,created_utc" + (before ? "&before=" + before : "");
        fetch(u).then(function (r) { return r.json(); }).then(function (j) {
          var d = j.data || [];
          d.forEach(function (p) {
            var text = ((p.title || "") + " " + (p.selftext || "")).toLowerCase(), hit = 0;
            words.forEach(function (w) { if (text.indexOf(w) >= 0) hit++; });
            if (hit >= Math.min(2, words.length) || (hit >= 1 && intent.test(text))) all.push(p);
          });
          if (d.length === 100 && n > 1) setTimeout(function () { page(sub, d[d.length - 1].created_utc, n - 1, done); }, 800);
          else done();
        }).catch(function () { errs++; done(); });
      }
      subs.forEach(function (sub, i) {
        setTimeout(function () { page(sub, null, 2, function () { if (--left === 0) cb({ posts: all, errors: errs }); }); }, i * 700);
      });
    }

    function render(idea, ranked, comps, top, subs, q, red) {
      var earners = top ? top.stats.tm_earners_1k : 0, topMrr = top ? top.stats.tm_top_mrr : 0;
      var verifiedComps = comps.filter(function (c) { return c.p.source === "trustmrr" && c.p.mrr; });
      var bestComp = verifiedComps.reduce(function (m, c) { return Math.max(m, c.p.mrr || 0); }, 0);
      var moneyPts = (bestComp >= 1000 || earners >= 2) ? 2 : (bestComp >= 200 || topMrr >= 500) ? 1 : 0;
      var n = red ? red.posts.length : null;
      var demandPts = n == null ? null : n >= 8 ? 2 : n >= 3 ? 1 : 0;
      var crowdPts = comps.length >= 8 ? 0 : comps.length >= 3 ? 1 : 2;
      var total = moneyPts + (demandPts || 0) + crowdPts;
      var grade = demandPts == null ? "…" : total >= 5 ? "A" : total >= 3 ? "B" : "C";
      var gradeTxt = { "A": "Strong evidence. Run the 72-hour test now.", "B": "Mixed evidence. Narrow to one buyer before testing.", "C": "Thin evidence. Treat as a hunch; find proof of payment first.", "…": "Checking Reddit…" }[grade];

      var h = '<section><div class="panel pad"><div class="row" style="gap:18px"><div class="grade grade-' + grade + '">' + grade + '</div><div><h2>Evidence grade</h2><p class="muted" style="margin:4px 0 0">' + esc(gradeTxt) + '</p></div></div>' +
        '<div class="bars" style="margin-top:14px;max-width:520px">' +
        bar("Money (verified)", moneyPts, bestComp ? "best comparable " + money(bestComp) + " MRR" : (topMrr ? "direction top " + money(topMrr) + " MRR" : "no verified revenue found")) +
        bar("Demand (Reddit, newest posts)", demandPts == null ? 0 : demandPts, n == null ? "checking…" : n + " matching posts for “" + q + "”") +
        bar("Room (fewer comparables)", crowdPts, comps.length + " comparable products in our data") + '</div></div></section>';

      h += '<section><div class="sec-head"><h2>Closest directions</h2></div>';
      if (!ranked.length) h += '<p class="empty">No direction matched. Try describing the buyer and the job, e.g. “invoice reminders for freelance designers”.</p>';
      else h += '<div class="grid g3">' + ranked.map(function (x) {
        var d = x.d;
        return '<div class="panel pad"><div class="row"><span class="badge v-' + d.verdict + '">' + d.verdict + '</span><span class="badge b-src">score ' + d.score.toFixed(2) + '</span></div>' +
          '<h3 style="margin-top:10px"><a href="directions/' + d.slug + '.html">' + esc(d.name) + '</a></h3><p class="small muted" style="margin-top:4px">' + esc(d.why) + '</p>' +
          '<div class="tiny faint" style="margin-top:10px"><span><b>' + d.stats.tm_players + '</b> verified players</span><span><b>' + d.stats.tm_earners_1k + '</b> at $1K+</span><span><b>' + d.stats.reddit_posts + '</b> intent posts/wk</span></div></div>';
      }).join("") + '</div>';
      h += '</section>';

      h += '<section><div class="sec-head"><div><h2>Comparable products</h2><p>Matched on your words. Verified = Stripe/RevenueCat-connected MRR on TrustMRR.</p></div></div>';
      if (!comps.length) h += '<p class="empty">No close comparables in our data. Either the niche is open or the words differ; check the direction pages.</p>';
      else h += '<div class="tbl-wrap"><table><thead><tr><th>Product</th><th>Source</th><th class="num">MRR</th></tr></thead><tbody>' + comps.map(function (c) {
        var p = c.p;
        return '<tr><td><a href="' + esc(p.url) + '" target="_blank" rel="noopener">' + esc(p.name) + '</a><span class="sub">' + esc(p.desc.slice(0, 140)) + '</span></td><td><span class="badge b-src">' + esc(p.source) + '</span></td><td class="num">' + (p.mrr ? money(p.mrr) + ' <span class="badge b-verified">verified</span>' : (p.rank ? "#" + p.rank + " grossing" : "–")) + '</td></tr>';
      }).join("") + '</tbody></table></div>';
      h += '</section>';

      h += '<section><div class="sec-head"><div><h2>Buyers talking on Reddit</h2><p>Live from Arctic Shift: r/' + subs.map(esc).join(", r/") + ' · newest ~200 posts each · matched on “' + esc(q) + '”</p></div></div>';
      if (!red) h += '<p class="empty">Searching…</p>';
      else if (!red.posts.length) h += '<p class="empty">No threads found' + (red.errors ? " (" + red.errors + " request errors)" : "") + '. Try fewer, plainer words.</p>';
      else {
        var posts = red.posts.slice().sort(function (a, b) { return (b.num_comments || 0) - (a.num_comments || 0); }).slice(0, 12);
        h += '<div class="panel threads">' + posts.map(function (p) {
          return '<div class="thread"><div class="c">' + (p.num_comments || 0) + ' replies</div><div class="t"><a target="_blank" rel="noopener" href="https://www.reddit.com/r/' + esc(p.subreddit) + '/comments/' + esc(p.id) + '/">' + esc(p.title) + '</a><div>r/' + esc(p.subreddit) + ' · u/' + esc(p.author) + '</div></div></div>';
        }).join("") + '</div>';
      }
      h += '</section>';

      h += '<section class="kit"><div class="sec-head"><h2>Your 72-hour validation kit</h2></div><div class="panel pad"><ol>' +
        '<li><span>Hour 1</span><div><b>Write the wedge in one line:</b> For <span class="slot">one buyer</span> who <span class="slot">has a pain from the threads above</span>, unlike <span class="slot">' + esc((comps[0] && comps[0].p.name) || "the current option") + '</span>, we <span class="slot">do one thing</span></div></li>' +
        '<li><span>Hour 4</span><div><b>Ship a landing page</b> with that line, one screenshot or mock, and an email or pre-order button.</div></li>' +
        '<li><span>Day 1</span><div><b>Post where buyers are:</b> ' + subs.map(function (s) { return '<a target="_blank" rel="noopener" href="https://www.reddit.com/r/' + esc(s) + '/">r/' + esc(s) + '</a>'; }).join(", ") + '. Answer the threads above; don’t spam.</div></li>' +
        '<li><span>Day 2</span><div><b>DM the people who asked.</b> The thread authors above are your first 20 interviews.</div></li>' +
        '<li><span>Day 3</span><div><b>Decide on day 3.</b> <span class="pass">Pass:</span> ≥ 5% of 200+ visitors leave an email, or ≥ 3 pre-pay. <span class="kill">Kill:</span> &lt; 2%, or every reply names an existing tool.</div></li></ol></div></section>';
      out.innerHTML = h;
    }
    function bar(k, pts, note) {
      return '<span>' + k + '</span><span class="bar"><i style="width:' + Math.round(pts / 2 * 100) + '%"></i></span><span class="tiny">' + esc(note) + '</span>';
    }
  }
})();
