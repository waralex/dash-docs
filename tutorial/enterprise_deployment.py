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
pip install dash-auth==0.0.4rc4
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
$ source venv/bin/activate
```

***

#### Step 3 - Add the following sample files to that folder

On your computer, create a new folder and add the
following files to that folder.
'''),

dcc.Markdown('''

Filename: **`app.py`**

Description: This file contains the actual Dash app code.

File Content:
'''),

dcc.SyntaxHighlighter('''import dash
import dash_auth
import dash_core_components as dcc
import dash_html_components as html
import os
import plotly.plotly as py

import config

app = dash.Dash(__name__)

# Expose the server variable
server = app.server

# Serve JS and CSS files locally instead of from global CDN
app.scripts.config.serve_locally = True
app.css.config.serve_locally = True
# https://my-dash-app-5.dash-qa.plotly.systems/_oauth
APP_URL = '{}://{}.{}'.format(
    config.PLOTLY_DASH_DOMAIN.split('://')[0],
    config.DASH_APP_NAME,
    config.PLOTLY_DASH_DOMAIN.split('://')[1]
)

dash_auth.PlotlyAuth(
    app,
    config.DASH_APP_NAME,
    config.DASH_APP_PRIVACY,
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

#### Step 4. Add a `config.py` file and modify with your account settings

Filename: **`config.py`**

Description: This file contains several settings that are used in your app.
It's kept in a separate file so that it's easy for you to transfer from
app to app. *Read through this file and modify the variables as appropriate.*

File content:
'''),

dcc.SyntaxHighlighter('''import os

# Replace with the name of your Dash app
# This will end up being part of the URL of your deployed app,
# so it can't contain any spaces, capitalizations, or special characters
DASH_APP_NAME = 'my-dash-app'

DASH_APP_PRIVACY = 'private'

# Fill in with your Plotly On-Premise username
os.environ['PLOTLY_USERNAME'] = 'your-plotly-username'

# Fill in with your Plotly On-Premise API key
# See <your-plotly-server>/settings/api to generate a key
# If you have already created a key and saved it on your own machine
# (from the Plotly-Python library instructions at https://plot.ly/python/getting-started)
# then you can view that key in your ~/.plotly/.config file or by running:
# `python -c import plotly; print(plotly.tools.get_config_file())`
os.environ['PLOTLY_API_KEY'] = 'your-plotly-api-key'

# Fill in with your Plotly On-Premise domain
os.environ['PLOTLY_DOMAIN'] = 'https://your-plotly-domain.com'
os.environ['PLOTLY_API_DOMAIN'] = os.environ['PLOTLY_DOMAIN']

# Fill in with the domain of your Dash subdomain.
# This matches the domain of the Dash App Manager
PLOTLY_DASH_DOMAIN='https://your-dash-manager-plotly-domain.com'

# Keep as True if your SSL certificates are valid.
# If you are just trialing Plotly On-Premise with self signed certificates,
# then you can set this to False. Note that self-signed certificates are not
# safe for production.
os.environ['PLOTLY_SSL_VERIFICATION'] = 'False'
''', language='python', customStyle=styles.code_container),

dcc.Markdown('''
As mentioned in the comments of the file, if you can generate your API key by
visiting <your-plotly-server>.com/settings/api.
If you have already generated an API key and saved it, then you can view it in
python with:
'''),

dcc.SyntaxHighlighter('''import plotly.tools as tls

print(tls.get_config_file())
''', language='python', customStyle=styles.code_container),

dcc.Markdown('''

***

#### Step 5. Test the app locally

Test that the files that you copied and pasted from the steps above work.

You can run the app locally with:
'''),

dcc.SyntaxHighlighter(
    '''$ python app.py''',
    language='python',
    customStyle=styles.code_container
),

dcc.Markdown('''
The default `DASH_APP_PRIVACY` setting in the `config.py` file adds a login
screen to this app. Your app should look like this and you should be able
to successfully log in.
'''),

html.Img(
    alt="Dash App Log In",
    src="https://github.com/plotly/dash-docs/raw/master/images/on-premise-local-login.gif",
    style={
        'width': '100%', 'border': 'thin lightgrey solid',
        'border-radius': '4px'
    }
),

dcc.Markdown('''
***

#### Step 5. Create an SSH key and add the SSH public key to the Dash App Manager

The SSH key is a way to authenticate you against the Plotly On Premise server.

To create an SSH key, run the following command. The command will walk you
through a few instructions.
'''),

dcc.SyntaxHighlighter(
    ('$ ssh-keygen -t rsa -b 4096 -C "your_email@example.com"'),
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
Open up the Dash App Manager and copy and paste this key. You can view this
key by running `$ cat ~/.ssh/plotly-ssh-key.pub` (replacing with the name
of your ssh key).

You can find the Dash App Manager by clicking on "Dash App" in your
Plotly On-Premise's "Create" menu.

> *The Dash App item in the Create menu takes you to the Dash App Manager*
'''),

html.Img(
    alt="Dash App Create Menu",
    src="https://github.com/plotly/dash-docs/raw/master/images/dash-create-menu.png",
    style={
        'width': '100%', 'border': 'thin lightgrey solid',
        'border-radius': '4px'
    }
),

dcc.Markdown('''
> *The Dash App Manager's SSH Key Interface. Copy and paste
> your public key in this interface and click "Update".*
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

#### Step 6. Add your App to the Dash App Manager

Visit the Dash App Manager. An item with the name that you specified in
the `config.py` file should appear. This item was created when you ran your
app locally in Step 5. Click on the `Add To This Server` button to register
the app to the Dash App Manager.

Once registered, you'll still need to add the Dash Enterprise server as your
git remote and push to fully deploy.
'''),

html.Img(
    alt="Dash App Manager Add App Interface",
    src="https://github.com/plotly/dash-docs/raw/master/images/dash-app-manager-launch-app.png",
    style={
        'width': '100%', 'border': 'thin lightgrey solid',
        'border-radius': '4px'
    }
),

dcc.Markdown('''
***

#### Step 7. Configure your Plotly Enterprise server to be your Git remote

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
`3022` but your server administrator may have set it to something different.

This file is located in `~/.ssh/config`. If it's not there, then create it.
You can open this file with `$ open ~/.ssh/config`. Add the following lines to
this file, replacing `your-dash-app-manager` with the domain of your
dash app manager (as you specified above):'''),

dcc.SyntaxHighlighter('''Host your-dash-app-manager
    Port 3022
'''),

dcc.Markdown('''***

#### Step 8. Add the Code and Deploy

Deploy your code by commiting it and pushing it to the repository:

'''),


dcc.SyntaxHighlighter('''git add .
git commit -m 'initial app'
git push plotly master
''', customStyle=styles.code_container, language='python'),


dcc.Markdown('''***

#### Step 9. Update the code and redeploy

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
