import dash_core_components as dcc

layout = dcc.Markdown('''
# Changelog

Updates and breaking changes from the dash community will be listed in
this changelog.

## dash-renderer [0.6.1] - 2017-05-09

### Fixed

`dash-renderer` version 0.6.1 fixes an intermittent bug
that occurs when certain requests take longer than
others to complete.

The bug manifests itself in a message that says
**Error loading layout** or sometimes
**Error loading dependencies**.

Upgrade with:
```
pip install dash-renderer==0.6.1
```
''')
