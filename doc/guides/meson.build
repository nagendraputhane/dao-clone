# SPDX-License-Identifier: Marvell-MIT
# Build multi-version HTML docs with sphinx-multiversion

sphinx_mv = find_program('sphinx-multiversion', required: false)
if not sphinx_mv.found()
  message('sphinx-multiversion not found; skipping user docs')
  subdir_done()
endif

# Files to trigger rebuilds when changed (not exhaustive, add more if you like)
docs_inputs = files(
  'conf.py',
  'index.rst',
  'guides.rst',
  'resources.rst',
)

# Also re-run when these assets change (keeps things fresh)
docs_assets = files(
  '_static/css/custom.css',
  '_static/js/titleprefix.js',
  '_static/js/version_switcher_match.js',
  '_static/versions.json',
)

# Output directory inside build tree
outdir = meson.current_build_dir() / 'html'

custom_target(
  'DAO Documentation (multi-version)',
  input:  docs_inputs + docs_assets,
  output: 'html',
  command: [
    sphinx_mv,
    '-v',                                  # verbose so CI shows the reason
    # Force only the remote 'origin' and exclude tags
    '-D', 'smv_remote_whitelist=^origin$',
    '-D', 'smv_branch_whitelist=^(dao-.*|dao-devel)$',
    '-D', 'smv_tag_whitelist=^$',
    # keep folder names as {ref.name}
    '-D', 'smv_outputdir_format={ref.name}',
    meson.current_source_dir(),
    outdir
  ],
  build_by_default: true,
  console: true,
  install: true,
  install_dir: join_paths(get_option('datadir'), 'doc', 'DAO', 'user-guide')
)