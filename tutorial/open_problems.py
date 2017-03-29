import dash_html_components as html
import dash_core_components as dcc


layout = dcc.Markdown('''
# Open Problems

### Multi-Page Apps

- An abstraction over react-router?
- Roll our own?
- Support anchor links?

### Saving and Loading Views

- If URLs are state, can this tie into multi-page apps?
- Ties into multi-page apps

### Front-end store

- Allow users to modify data through events

### Hotloading

- Use flask-sockets
- Re-run the initialization steps in the front-end
- Tie into general websockets framework?

### Layouts

- Report layout
- App layout
- Container layout

### Authentication and saving

- Oauth
- Keep as much logic in front end so that other languages can just use
  dash-renderer

### ID-Groups

- Register callbacks on groups of elements
- Allows arbitrary number of elements to be created, e.g. TODO MVP

### Caching requests in front end

- Caching on by default, turn it off with a decorator

```
@dash.caching('off')
@dash.callback(...)
def realtime_data(...):
    ...
```

### Finalize variable names

**`Input`, `Output`**
```
from dash.dependencies import Input, Output

from dash.decorators import Input, Output
```

### New Components

**Typeahead Input**
```
@app.callback(
    Input('my-input', 'typeaheadOptions'),
    [Input('my-input', 'value')]
)
def update_typeahead_options(value):
    return get_list_of_options(startsWith=value)[0:5]
```

**Interactive Table**

- Specify types for numbers, decimal places, dates, categories
- Editable
- Sortable

**Date, Time, Week Inputs**

- [http://react-component.github.io/calendar/](http://react-component.github.io/calendar/)

**Upload**


**Tabs**


''')
