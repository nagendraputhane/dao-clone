# SPDX-License-Identifier: Marvell-MIT
# Build multi-version HTML docs with sphinx-multiversion

sphinx_mv = find_program('sphinx-multiversion', required: false)
if not sphinx_mv.found()
  message('sphinx-multiversion not found; skipping user docs')
  subdir_done()
endif

docs_inputs = files(
  'conf.py',
  'index.rst',
  'guides.rst',
  'resources.rst',
)

docs_assets = files(
  '_static/css/custom.css',
  '_static/js/titleprefix.js',
  '_static/js/version_switcher_match.js',
  '_static/versions.json',
)

outdir = join_paths(meson.current_build_dir(), 'html')

custom_target(
  'DAO Documentation (multi-version)',
  input:  docs_inputs + docs_assets,
  output: 'html',  # directory created by sphinx-multiversion
  command: [
    sphinx_mv,
    '-vv',
    meson.current_source_dir(),
    outdir
  ],
  build_by_default: true,
  install: true,
  install_dir: join_paths(get_option('datadir'), 'doc', 'DAO', 'user-guide')
)
