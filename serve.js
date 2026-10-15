/* Attelkom Jarnama ad server.
   <script src="https://mjsbroadbent.github.io/jarnama/serve.js" data-site="herald" defer></script>
   <div class="jarnama" data-size="728x90"></div>
   Each slot gets a random active ad of its size for this site; empty slots stay hidden. */
(function () {
  var me = document.currentScript;
  var base = me.src.replace(/serve\.js.*$/, "");
  var site = me.getAttribute("data-site") || "all";
  function today() { return new Date().toISOString().slice(0, 10); }
  function fill(ads) {
    var slots = document.querySelectorAll(".jarnama[data-size]");
    Array.prototype.forEach.call(slots, function (slot) {
      var size = slot.getAttribute("data-size"), t = today();
      var pool = ads.filter(function (a) {
        return a.active !== false && a.size === size &&
          (!a.sites || a.sites.indexOf("all") >= 0 || a.sites.indexOf(site) >= 0) &&
          (!a.start || a.start <= t) && (!a.end || a.end >= t);
      });
      if (!pool.length) { slot.style.display = "none"; return; }
      var ad = pool[Math.floor(Math.random() * pool.length)];
      var wh = size.split("x"), w = wh[0], h = wh[1], src = base + ad.file;
      var inner = /\.html?$/.test(ad.file)
        ? '<iframe src="' + src + '" width="' + w + '" height="' + h + '" scrolling="no" frameborder="0" title="' + (ad.alt || "Advertisement") + '"></iframe>'
        : '<img src="' + src + '" width="' + w + '" height="' + h + '" alt="' + (ad.alt || "") + '">';
      slot.innerHTML = '<a href="' + (ad.link || "#") + '" rel="sponsored noopener" target="_blank">' + inner + "</a>";
      slot.style.display = "";
    });
  }
  fetch(base + "campaigns.json", { cache: "no-cache" }).then(function (r) { return r.json(); })
    .then(function (d) { fill(d.ads || []); }).catch(function () {});
})();
