import dash_core_components as dcc
import dash_html_components as html
import styles

layout = [dcc.Markdown('''
# Deploying Dash Apps on Plotly On-Premise

By default, Dash apps run on `localhost` - you can only access them on your
own machine. With Plotly On-Premise, you can easily deploy your Dash code
to your organization's behind-the-firewall server.
If you would like to learn more about Plotly On-Premise or start a trial,
[please reach out](https://plotly.typeform.com/to/seG7Vb).

### Getting Started Guide

***

#### Step 1. Create a new folder for your project

For example:
'''),

dcc.SyntaxHighlighter('''mkdir dash_app_example
cd dash_app_example
''', customStyle=styles.code_container),

dcc.Markdown('''
***

#### Step 2. Initialize that folder with `git` and a `virtualenv`

'''),

dcc.SyntaxHighlighter('''git init        # initializes an empty git repo
virtualenv venv # creates a virtualenv called "venv"
source venv/bin/activate # uses the virtualenv
''', customStyle=styles.code_container),

dcc.Markdown('''
`virtualenv` creates a fresh Python instance. You will need to reinstall your
app's dependencies with this virtualenv:
'''),

dcc.SyntaxHighlighter('''pip install dash==0.17.8rc2
pip install dash-auth==0.0.2
pip install dash-renderer
pip install dash-core-components
pip install dash-html-components
pip install plotly
pip install gunicorn
''', customStyle=styles.code_container),

dcc.Markdown('''

Anytime that you want to do work on this app inside this folder, you should
make sure that you're using this project's `virtualenv`.
Activate the `virtualenv` with
```
source venv/bin/activate
```

***

#### Step 3 - Add the following sample files to that folder

On your computer, create a new folder and add the
following files to that folder.

Filename: **`app.py`**

Description: This file contains the actual Dash app code.

Dash code that is deployed on Plotly Enteprise requires a few modifications.
These modifications are noted in the code below:
- Signing in to your Plotly account
- Adding a secret key
- Adding Plotly authentication
- Serving source files locally (optional)

File Content:
'''),

dcc.SyntaxHighlighter('''import dash
import dash_auth
import dash_core_components as dcc
import dash_html_components as html
import plotly.plotly as py

import config

app = dash.Dash(__name__)

# Expose the server variable
server = app.server

# Serve JS and CSS files locally instead of from global CDN
app.config.scripts.serve_locally = True
app.config.css.serve_locally = True

# Set the server secret key - this variable is set through the `.env` file
server.secret_key = os.environ.get('SECRET_KEY', 'my-secret-key')

py.sign_in(
    config.PLOTLY_USERNAME,
    config.PLOTLY_API_KEY,
    plotly_domain=config.PLOTLY_DOMAIN,
    plotly_api_domain=config.PLOTLY_DOMAIN, # same as plotly_domain
)

# Set the privacy of your Dash app. This also saves the app to your
# Plotly on-premise account where you can manage its permissions at
# https://<your-plotly-server>/organize

# Modify these variables with your own info
APP_NAME = 'dash-sample-app'
APP_URL = '{}://{}.{}'.format(
    PLOTLY_DOMAIN.split('://')[0],
    APP_NAME,
    PLOTLY_DOMAIN.split('://')[1]
)

# 'private' means that you need to login to view it. You can authorize other
# viewers to your app in your list of files at
# https://<your-plotly-server>/organize
# 'public' means that anyone who has access to your
# plotly server can view the app
APP_PRIVACY = 'private'

dash_auth.PlotlyAuth(
    app,
    APP_NAME,
    APP_PRIVACY,
    APP_URL
)

# Standard Dash app code below
app.layout = html.Div([
    html.H2('Hello World'),
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': i, 'value': i} for i in ['LA', 'NYC', 'MTL']],
        value='LA'
    ),
    html.Div(id='display-value')
])

@app.callback(dash.dependencies.Output('display-value', 'children'),
              [dash.dependencies.Input('dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)

if __name__ == '__main__':
    app.run_server(debug=True)
''', customStyle=styles.code_container, language='python'),

dcc.Markdown('''
***

Filename: **`.gitignore`**

Description: This file specifies which files should not be included in the Git repository.

File content:
'''),

dcc.SyntaxHighlighter('''venv
*.pyc
.DS_Store
''', customStyle=styles.code_container),

dcc.Markdown('''
***

Filename: **`Procfile`**

Description: This file provides the Dash deployment server with the set of commands to run
the server. In this case, we're running a "web" process and runs the command
`gunicorn app:server`. You can test this yourself by running that command in
your terminal. Note that `app` refers to the filename `app.py` and `server`
refers to the variable `server` inside that file.

File content:
'''),

dcc.SyntaxHighlighter('''web: gunicorn app:server
''', customStyle=styles.code_container),

dcc.Markdown('''

***

Filename **`requirements.txt`**

Description: `requirements.txt` describes your Python dependencies.
You can fill this file in automatically with:
'''),

dcc.SyntaxHighlighter('''$ pip freeze > requirements.txt
''', customStyle=styles.code_container),

dcc.Markdown('''
***

Filename: **`config`**

Description: This file contains several settings that are used in your app.
It's kept in a separate file so that it's easy for you to transfer from
app to app.

File content:
'''),

dcc.SyntaxHighlighter('''# Fill in with your Plotly On-Premise username
PLOTLY_USERNAME='my-plotly-username'

# Fill in with your Plotly On-Premise API key
# See <your-plotly-server>/settings/api to generate a key
# If you have already created a key and saved it on your own machine
# (from the Plotly-Python library instructions at https://plot.ly/python/getting-started)
# then you can view that key in your ~/.plotly/.config file or by running:
# `python -c import plotly; print(plotly.tools.get_config_file())`
PLOTLY_API_KEY='my-plotly-api-key'

# Fill in with your Plotly On-Premise domain
PLOTLY_DOMAIN='https://plotly.acme-corporation.com'
''', language='python', customStyle=styles.code_container),

dcc.Markdown('''
As mentioned in the comments, if you can generate your API key by
visiting <your-plotly-server>.com/settings/api.
If you have already generated an API key and saved it, then you can view it in
python with:
'''),

dcc.SyntaxHighlighter('''import plotly.tools as tls

print(tls.get_config_file())
''', language='python', customStyle=styles.code_container),

dcc.Markdown('''

***

#### Step 4. Create an SSH key and add the SSH public key to the Dash App Manager

The SSH key is a way to authenticate you against the Plotly On Premise server.

To create an SSH key, run the following command. The command will walk you
through a few instructions. You can modify `~/.ssh/plotly-ssh-key` to a
different location if you would like.
'''),

dcc.SyntaxHighlighter(
    ('$ ssh-keygen -t rsa -b 4096 -C "your_email@example.com" '
     '-f "~/.ssh/plotly-ssh-key"'),
    customStyle=styles.code_container,
    language='python'
),

dcc.Markdown('''
This will create two files in the location that you have specified.
One of these files is the "public key" and it contains the ".pub" suffix.

Add this SSH key to your system with the `ssh-add` command.
For example, if your key was created in the location `~/.ssh/plotly-ssh-key`,
then run:
'''),

dcc.SyntaxHighlighter(
    '$ ssh-add ~/.ssh/plotly-ssh-key',
    customStyle=styles.code_container,
    language='python'
),

dcc.Markdown('''
Open up the Dash App Manager and copy and paste this key.
You can find the Dash App Manager by clicking on "Dash App" in your
Plotly On-Premise's "Create" dropdown.
'''),

html.Img(
    alt="Dash App Manager Public Key Interface",
    src="https://github.com/plotly/dash-docs/raw/master/images/dash-app-manager-ssh-key.png",
    style={
        'width': '100%', 'border': 'thin lightgrey solid',
        'border-radius': '4px'
    }
),

dcc.Markdown('''
***

#### Step 5. Create a Dash App in the Dash App Manager

Visit the Dash App Manager and create a Dash app. The app name will be used
in the URL of the app. For example, an app with the name `my-dash-app` will be
accessible at the URL
`my-dash-app.your-dash-app-manager.your-plotly-server.com`
or, if path-based routing is set up, 'your-plotly-server/my-dash-app'.

'''),

html.Img(
    alt="Dash App Manager Add App Interface",
    src="https://github.com/plotly/dash-docs/raw/master/images/dash-app-manager-add-app-interface.gif",
    style={
        'width': '100%', 'border': 'thin lightgrey solid',
        'border-radius': '4px'
    }
),

dcc.Markdown('''
***

#### Step 6. Configure your Plotly Enterprise server to be your Git remote

Your application code will be transferred to the Dash Enterprise server through
`git` and `ssh`.

The following command will create a remote host to your new app on
Plotly Enterprise.
'''),


dcc.Markdown('''
Replace `your-dash-app-name` with the name of your Dash app that you supplied
in the Dash app manager and `your-dash-app-manager` with the domain of the
Dash App Manager. For example, if your Dash app name was `my-first-dash-app`
and the domain of your organizations Dash App Manager was `dash.plotly.acme-corporation.com`,
then this command would be
`git remote add plotly dokku@dash.plotly.acme-corporation.com:my-first-dash-app`:
'''),

dcc.SyntaxHighlighter(
    '$ git remote add plotly dokku@your-dash-app-manager:your-dash-app-name',
    customStyle=styles.code_container,
    language='python'
),

dcc.Markdown('''
Next, specify a custom port in your SSH config. By default, this should be
`3022` but your server administrator may set it to something different.

This file is located in `~/.ssh/config`. If it's not there, then create it.
You can open this file with `$ open ~/.ssh/config`. Add the following lines to
this file, replacing `your-dash-app-manager` with the domain of your
dash app manager (as you specified above):'''),

dcc.SyntaxHighlighter('''Host your-dash-app-manager
    Port 3022
'''),

dcc.Markdown('''***

#### Step 7. Add the Code and Deploy

Deploy your code by commiting it and pushing it to the repository:

'''),


dcc.SyntaxHighlighter('''git add .
git commit -m 'initial app'
git push plotly master
''', customStyle=styles.code_container, language='python'),


dcc.Markdown('''***

#### Step 8. Update the code and redeploy

When you modify `app.py` with your own code, you will need to add the changes
to git and push those changes to heroku.
'''),

dcc.SyntaxHighlighter('''$ git status # view the changed files
$ git diff # view the actual changed lines of code
$ git add .  # add all the changes
$ git commit -m 'a description of the changes'
$ git push plotly master
''', customStyle=styles.code_container, language='python')

]
