# SPDX-License-Identifier: Marvell-MIT

sphinx = find_program('sphinx-build', required: false)
if not sphinx.found()
  sphinx = find_program('sphinx-build-3', required: false)
endif
if not sphinx.found()
  message('sphinx-build not found; skipping Guides (single-version).')
  subdir_done()
endif

# Minimal inputs (add more files if you want Meson to re-run when they change)
docs_inputs = files(
  'conf.py',
  'index.rst',
  'guides.rst',
  'resources.rst',
)

# Assets that are safe to track (fine even if SMV also uses them later)
docs_assets = files(
  '_static/css/custom.css',
  '_static/js/titleprefix.js',
  '_static/js/version_switcher_match.js',
  '_static/versions.json',
)

outdir = meson.current_build_dir() / 'html-single'

custom_target(
  'DAO Documentation (single-version)',
  input:  docs_inputs + docs_assets,
  output: 'html-single',
  command: [sphinx, '-q', '-W', '-b', 'html', meson.current_source_dir(), outdir],
  build_by_default: true,
  console: true,
  install: true,
  install_dir: join_paths(get_option('datadir'), 'doc', 'DAO', 'user-guide')
)
