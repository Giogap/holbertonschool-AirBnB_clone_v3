#!/usr/bin/python3
'''
    app for registering blueprint and starting flask
'''
from flask import Flask, make_response, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def tear_down(self):
    '''
    close query after each session
    '''
    storage.close()


@app.errorhandler(404)
def not_found(error):
    '''
    return JSON formatted 404 status code response
    '''
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    port = getenv("HBNB_API_PORT", default=5000)
    host = getenv("HBNB_API_HOST", default="0.0.0.0")
    app.run(host=host, port=port, threaded=True, debug=True)