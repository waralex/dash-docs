# Dash Userguide

The [Dash Userguide](https://plotly.com/dash): everything that you need to know to be productive with Dash.

The Dash Userguide is hosted online at: [https://plotly.com/dash](https://plotly.com/dash). 

### Running an app locally

To run an app locally:

1. (optional) create and activate new virtualenv or conda env:

```
pip install virtualenv
virtualenv venv
source venv/bin/activate
```

or, with conda:
```
conda create --yes -n dash_docs
source activate dash_docs
```

2. `pip install -r requirements.txt`
3. `gunicorn --preload index:server` 

Alternatively, for development purposes, you can run:
`while true; do IGNORE_DASH_BIO=true python index.py; sleep 2; done`

The `while true` loop restarts Dash when there's syntax errors outside of the callbacks, 
and `IGNORE_DASH_BIO=true` constant prevents the loading of heavy Dash Bio examples, which makes hotreloading faster.

4. open http://127.0.0.1:8000 in your browser


on Windows systems `waitress` can be a replacement for `gunicorn`

3. `pip install waitress`
4. `waitress-serve --listen=*:8000 index:server`
5. open http://127.0.0.1:8000 in your browser


### Contributing

PRs accepted! The Dash user guide is itself a Dash app. Each file in `tutorial` represents a "chapter" of the docs.

Changes to master will get deployed automatically.

Note: In the past, some corporate networks have blocked our website at https://dash.plot.ly. We created a PDF for those community members.

We have since resolved these issues by moving to https://dash.plotly.com and we’ve stopped maintaining this PDF documentation.

Is your network still blocking our docs and do you still need a PDF version?

If so, please comment on this issue: https://github.com/plotly/dash-docs/issues/897A. 
