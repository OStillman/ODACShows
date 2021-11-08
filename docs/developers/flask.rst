ODAC Flask Setup
================

App.py
------

App.py is the main entry point for the flask app. 

You'll notice the use of a blueprint for entry_point control. This keeps this app.py file clear, concise, and for one purpose. 

`app.register_blueprint(endpoint_control, url_prefix='/ODAC/shows')`

The flask app's URL entry points are therefore controlled in endpoints\endpoint_control.py