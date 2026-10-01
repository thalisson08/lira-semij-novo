from flask import Flask

from app.routes import api


def create_app(testing=False):
    app = Flask(__name__)
    app.config["TESTING"] = testing
    app.register_blueprint(api)
    return app
