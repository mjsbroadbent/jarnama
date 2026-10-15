/* Attelkom Jarnama ad server.
   <script src="https://mjsbroadbent.github.io/jarnama/serve.js" data-theme="current state" defer></script>
   <div class="jarnama" data-size="728x90"></div>
   <div class="jarnama" data-size="240x400" data-theme="sketchy"></div>   (a slot can override the theme)
   Each slot gets a random active ad of its size whose themes overlap the slot's; empty slots stay hidden.
   Themes are listed in THEMES.md. */
(function () {
  var me = document.currentScript;
  var base = me.src.replace(/serve\.js.*$/, "");
  var pageThemes = (me.getAttribute("data-theme") || "current").split(/\s+/);
  function today() { return new Date().toISOString().slice(0, 10); }
  function fill(ads) {
    var slots = document.querySelectorAll(".jarnama[data-size]");
    Array.prototype.forEach.call(slots, function (slot) {
      var size = slot.getAttribute("data-size"), t = today();
      var want = slot.getAttribute("data-theme") ? slot.getAttribute("data-theme").split(/\s+/) : pageThemes;
      var pool = ads.filter(function (a) {
        return a.active !== false && a.size === size &&
          (a.themes || []).some(function (th) { return want.indexOf(th) >= 0; }) &&
          (!a.start || a.start <= t) && (!a.end || a.end >= t);
      });
      if (!pool.length) { slot.style.display = "none"; return; }
      var ad = pool[Math.floor(Math.random() * pool.length)];
      var wh = size.split("x"), w = wh[0], h = wh[1], src = base + ad.file;
      var inner = /\.html?$/.test(ad.file)
        ? '<iframe src="' + src + '" width="' + w + '" height="' + h + '" scrolling="no" frameborder="0" title="' + (ad.alt || "Advertisement") + '"></iframe>'
        : '<img src="' + src + '" width="' + w + '" height="' + h + '" alt="' + (ad.alt || "") + '">';
      var href = !ad.link ? "#" : /^https?:/.test(ad.link) ? ad.link : base + ad.link;
      slot.innerHTML = '<a href="' + href + '" rel="sponsored noopener" target="_blank">' + inner + "</a>";
      slot.style.display = "";
    });
  }
  fetch(base + "campaigns.json", { cache: "no-cache" }).then(function (r) { return r.json(); })
    .then(function (d) { fill(d.ads || []); }).catch(function () {});
})();
