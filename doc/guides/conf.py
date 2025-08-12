# SPDX-License-Identifier: Marvell-MIT
# Main Sphinx configuration for DAO docs
# ---------------------------------------------------------------------------

from datetime import datetime

project   = "Data Accelerator Offload"
author    = "Marvell"
release   = "25.05.0"
copyright = f"2024-{datetime.now().year}, Marvell"
html_logo = "logo/dao_logo.png"
master_doc = "index"

# ---------------------------------------------------------------------------
extensions = ["sphinx_copybutton", "sphinx_multiversion", "sphinx_design"]

smv_branch_whitelist = r"^dao-.*|^dao-devel$"
smv_tag_whitelist    = r"^$"
smv_remote_whitelist = r"^origin$"
smv_outputdir_format = "{ref.name}"

# ---------------------------------------------------------------------------
html_theme = "pydata_sphinx_theme"
version    = "dao-devel"                           # this branch’s label

html_context = {"version": version}

html_theme_options = {
    "switcher": {
        "json_url": "https://nagendraputhane.github.io/dao-clone/versions.json",
        "version_match": version,
    },
    "external_links": [
        {"name": "Home", "url": "https://nagendraputhane.github.io/dao-clone/"},
    ],
    "icon_links": [
        {
            "name": "GitHub Repo",
            "url": "https://github.com/nagendraputhane/dao-clone",
            "icon": "fa-brands fa-github",
            "type": "fontawesome",
        },
    ],
    "default_mode": "light",                       # light-only
    "navbar_end": ["search-button",
                   "version-switcher",
                   "navbar-icon-links"],
}

html_meta = {
    "color-scheme": "light",
}

html_static_path   = ["_static"]
html_css_files     = ["css/custom.css"]
html_js_files = [
    "js/version_switcher_match.js",
]

html_favicon       = "_static/tab_logo.jpg"
html_show_sourcelink = False


html_sidebars = {
    "index": [],
}

exclude_patterns   = ["_build", "Thumbs.db", ".DS_Store"]

templates_path = ["_templates"]