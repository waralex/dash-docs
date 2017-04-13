from server import app


def load_example(path):
    with open(path, 'r') as _f:
        _source = _f.read()
        _example = _source

        # Use the global app assignment
        if 'app = dash.Dash' not in _example:
            raise Exception("Didn't declare app")
        _example = _example.replace('app = dash.Dash', '# app = dash.Dash')

        if 'import dash\n' not in _example:
            raise Exception("Didn't import dash")

        # return the layout instead of assigning it to the global app
        if 'app.layout = ' not in _example:
            raise Exception("app.layout not assigned")
        _example = _example.replace('app.layout = ', 'layout = ')

        # Remove the "# Run the server" commands
        if 'app.run_server' not in _example:
            raise Exception("app.run_server missing")
        _example = _example.replace(
            '\n    app.run_server',
            'print("Running")\n    # app.run_server'
        )

        exec(_example, globals(), globals())

    return (
        _source,
        layout      # layout is a global created from the app
    )
