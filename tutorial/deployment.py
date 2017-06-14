import dash_core_components as dcc

layout = dcc.Markdown('''
# Deploying Apps

Dash apps run the Flask web-server under the hood. If you can deploy a Flask
application, then you can deploy a Dash app.
There are many services available for deploying apps on the public cloud:
Heroku, Digital Ocean, Amazon Web Services, Google Cloud.

For enterprises, we offer a Dash Enterprise Add-on to Plotly On-Premise.
Dash Enterprise provides you with a plug-and-play deployment and permissioning
server. Provisioning and managing server applications is usually a full-time
job. Dash Enterprise abstracts away all of the complexity with updating and
managing behind-the-firewall server applications.

[Request a Dash Enterprise demo](https://plot.ly/products/on-premise).

''')
