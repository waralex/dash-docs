# Debugging & Development Workflow

## Code Editor Recommendations

VSCode, DE Workspaces, Jupyter

## Editor vs Jupyter

> I like both!
> You don't have to choose, JupyterDash is perfectly fine

In support of editors
- Multipage apps
- Debugging
- Function lookup
- A bunch of reasons why jupyter xyz
- Diffs
- Command line tools like Celery

In support of Jupyter
- Repl life
- Rich outputs
- Caching

## Debugging Workflows

1. `print`. Consider `pprint` or in Jupyter `display`
2. `import ipdb; ipdb.set_trace()`
3. VSCode built-in debugger
4. Jupyter debugger??
5. Moving between Editor and Jupyter
6. Examining values in dev tools

## Interpreting error messages from Dash Dev tools?

## Moving Between Editor and Jupyter

`pkl.py`
```python
```

In your code, place a `gherkin.dump()` where you want to save the files
```python
@app.callback()
def update():
    gherkin.dump(globals(), locals())
```

Then, load those variables into your Jupyter or IPython session for examination
with
```python
gherkin.load(locals())
```

Now you can use the Jupyter Variable Explorer among other tools.

Notes:
- Keep Jupyter (kernel) and Python used to run Dash (a virtual env)  in sync.
In DE, these are one and the same
- `gherkin.load(locals())` will inject the variables into your Jupyter namespace,
overwriting any variables that have the same name. To save them to a separate namespace, you can do:
    ```python
    data = {}
    gherkin.load(data)
    ```
- Uses pickle, is not secure for anything besides debugging. And don't load someone else's file!
- Once in Jupyter, you can write your callback code and copy and paste it back into Dash.
The Dash file is like a "hardened" version of the code.
- Consider importing `app.py` too to call functions
    - Consider using `importlib` and `importlib.reload()`
- In this workflow, Jupyter is like a scratch pad

## Modularizing into Separate Files & Functions
- Unit tests
- Importing into Jupyter etc
- Composability
- Keep components with callbacks together. MVC is overrated
- Folder structure:
    - `pages/`
    - `components/`
    - `utils.py`
    - `styles.py`
    - `data/`
    - `scratch-pad.ipynb`

## Jupyter Workflow
- Each function & callback is a cell
- You only need to re-run that cell
- Use `display` or w/e
- `ipdb/pdb` doesn't work but not sure
- As your code "hardens", split out into files and import
- Jupytext?

## Reusable Functions
```python
def InteractiveTable(**kwargs):
    return DataTable(editable='native', sortable='native', filtering='native', **kwargs)
```

## Tips & Tricks from the Community

> Keyboard shortcuts for moving around with arrows
> Split screen & keyboard shortcuts
