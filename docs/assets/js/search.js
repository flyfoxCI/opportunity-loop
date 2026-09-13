/* Opportunity Loop — client-side search + theme toggle
   Loaded at the bottom of every page. No dependencies. */

(function () {
  'use strict';

  // ============================================================
  // Theme toggle (dark mode)
  // ============================================================
  const THEME_KEY = 'opportunity-loop-theme';
  const root = document.documentElement;

  function applyTheme(theme) {
    if (theme === 'dark') {
      root.setAttribute('data-theme', 'dark');
      const icon = document.getElementById('theme-icon');
      if (icon) icon.textContent = '☀';
    } else {
      root.removeAttribute('data-theme');
      const icon = document.getElementById('theme-icon');
      if (icon) icon.textContent = '☾';
    }
  }

  // Load saved theme; fall back to system preference
  let savedTheme = null;
  try { savedTheme = localStorage.getItem(THEME_KEY); } catch (e) {}
  if (!savedTheme) {
    savedTheme = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }
  applyTheme(savedTheme);

  // Wire up the toggle button
  document.addEventListener('DOMContentLoaded', function () {
    const toggleBtn = document.getElementById('theme-toggle');
    if (toggleBtn) {
      toggleBtn.addEventListener('click', function () {
        const current = root.getAttribute('data-theme') === 'dark' ? 'dark' : 'light';
        const next = current === 'dark' ? 'light' : 'dark';
        applyTheme(next);
        try { localStorage.setItem(THEME_KEY, next); } catch (e) {}
      });
    }
  });

  // ============================================================
  // Search (loads /search.json, fuzzy-filters in-browser)
  // ============================================================
  const SEARCH_URL = '/opportunity-loop/search.json';
  let searchIndex = null;

  function loadIndex(cb) {
    if (searchIndex) return cb(searchIndex);
    fetch(SEARCH_URL, { credentials: 'omit' })
      .then(function (r) { if (!r.ok) throw new Error('search.json HTTP ' + r.status); return r.json(); })
      .then(function (data) { searchIndex = data; cb(data); })
      .catch(function (err) {
        console.warn('[search] failed to load index:', err);
        cb(null);
      });
  }

  function score(post, terms) {
    const haystack = (
      (post.title || '') + ' ' +
      (post.excerpt || '') + ' ' +
      (post.tags || []).join(' ') + ' ' +
      (post.tier || '')
    ).toLowerCase();
    let s = 0;
    for (const t of terms) {
      if (!t) continue;
      if (haystack.includes(t)) s += 2;
      // bonus for title match
      if ((post.title || '').toLowerCase().includes(t)) s += 3;
      // bonus for tag match
      if ((post.tags || []).some(function (tag) { return tag.toLowerCase() === t; })) s += 4;
    }
    return s;
  }

  function highlight(text, terms) {
    if (!terms.length || !text) return text;
    const re = new RegExp(
      '(' + terms.filter(Boolean).map(function (t) { return t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'); }).join('|') + ')',
      'gi'
    );
    return text.replace(re, '<mark>$1</mark>');
  }

  function render(posts, terms) {
    const results = document.getElementById('site-search-results');
    if (!results) return;
    if (!posts.length) {
      results.innerHTML = '<div class="site-nav__result-empty">No matches</div>';
      results.classList.add('is-open');
      return;
    }
    results.innerHTML = posts.slice(0, 12).map(function (p) {
      const tierPill = p.tier
        ? '<span class="pill pill--' + (p.tier === 'GO' ? 'go' : 'narrow') + '">' + p.tier + '</span> '
        : '';
      const date = p.date ? p.date.slice(0, 10) : '';
      return (
        '<a class="site-nav__result" href="' + p.url + '">' +
          '<div class="site-nav__result-title">' + highlight(p.title || '', terms) + '</div>' +
          '<div class="site-nav__result-meta">' + tierPill +
            (date ? date : '') +
            (p.tags && p.tags.length ? ' · ' + p.tags.slice(0, 4).map(function (t) { return '#' + t; }).join(' ') : '') +
          '</div>' +
        '</a>'
      );
    }).join('');
    results.classList.add('is-open');
  }

  document.addEventListener('DOMContentLoaded', function () {
    const input = document.getElementById('site-search');
    const results = document.getElementById('site-search-results');
    if (!input || !results) return;

    // Load the index eagerly (so first keystroke is fast)
    loadIndex(function () { /* cached */ });

    input.addEventListener('input', function () {
      const q = input.value.trim().toLowerCase();
      if (!q) {
        results.classList.remove('is-open');
        results.innerHTML = '';
        return;
      }
      const terms = q.split(/\s+/).filter(function (t) { return t.length >= 2; });
      if (!terms.length) {
        results.classList.remove('is-open');
        return;
      }
      loadIndex(function (data) {
        if (!data || !data.posts) {
          results.innerHTML = '<div class="site-nav__result-empty">Search unavailable</div>';
          results.classList.add('is-open');
          return;
        }
        const matches = data.posts
          .map(function (p) { return { p: p, s: score(p, terms) }; })
          .filter(function (x) { return x.s > 0; })
          .sort(function (a, b) { return b.s - a.s; })
          .map(function (x) { return x.p; });
        render(matches, terms);
      });
    });

    input.addEventListener('focus', function () {
      if (input.value.trim()) {
        results.classList.add('is-open');
      }
    });

    document.addEventListener('click', function (e) {
      if (!input.contains(e.target) && !results.contains(e.target)) {
        results.classList.remove('is-open');
      }
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && results.classList.contains('is-open')) {
        results.classList.remove('is-open');
        input.blur();
      }
      // Cmd/Ctrl-K focuses search
      if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
        e.preventDefault();
        input.focus();
        input.select();
      }
    });
  });
})();
