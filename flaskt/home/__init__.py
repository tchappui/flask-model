import flask

home = flask.Blueprint("home", __name__)

from . import views
