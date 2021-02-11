from flask import Flask, flash, redirect, url_for, render_template, request

from endpoints.endpoint_control import endpoint_control

from endpoints.api_endpoint_control import api_endpoint_control

app = Flask(__name__)

app.register_blueprint(endpoint_control, url_prefix='/ODAC/shows')

app.register_blueprint(api_endpoint_control, url_prefix='/ODAC/shows/api')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')