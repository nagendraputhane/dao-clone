// Keep the version switcher label in sync with the URL (works with sphinx-multiversion)
(function () {
  function currentVersionFromPath() {
    var m = (location.pathname || "").match(/\/dao-clone\/([^/]+)\//);
    return (m && m[1]) ? m[1] : "dao-devel";  // default on site root
  }
  function labelFor(v) {
    if (v === "dao-devel") return "latest (dev)";
    var m = v.match(/^dao-(.+)$/);
    return m ? m[1] : v;
  }
  var v = currentVersionFromPath();

  // Update the config (used by theme scripts)
  if (window.DOCUMENTATION_OPTIONS) {
    window.DOCUMENTATION_OPTIONS.theme_switcher_version_match = v;
  }

  // After the theme initializes, fix the button label & active item.
  function apply() {
    try {
      var btn = document.querySelector('[id^="pst-version-switcher-button"]');
      if (!btn) return;

      // Set button text
      // Button text node is the first child text; safest approach: overwrite textContent.
      btn.childNodes[0] && (btn.childNodes[0].nodeValue = labelFor(v));
      btn.textContent = labelFor(v);

      // Mark active item in the dropdown if it’s been built
      var menuId = btn.getAttribute("aria-controls");
      var menu = menuId && document.getElementById(menuId);
      if (menu) {
        var items = menu.querySelectorAll("a.dropdown-item");
        items.forEach(function (a) {
          var href = a.getAttribute("href") || "";
          var active = href.indexOf("/" + v + "/") !== -1;
          a.classList.toggle("active", active);
          if (active) a.setAttribute("aria-current", "true");
          else a.removeAttribute("aria-current");
        });
      }
    } catch (e) {}
  }

  // Run after DOM ready, then again after theme finishes populating
  document.addEventListener("DOMContentLoaded", function () {
    apply();
    setTimeout(apply, 100);
    setTimeout(apply, 600);
  });
})();
