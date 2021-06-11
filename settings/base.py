import os
import pathlib


BASE_DIR = pathlib.Path(__file__).resolve().parent

INSTALLED_BLUEPRINTS = [
    {"module": "flaskt.home", "name": "home", "prefix": ""}
]

SECRET_KEY = os.environ.get("SECRET_KEY", "very secret and unguessable value")

SQLALCHEMY_TRACK_MODIFICATIONS = False
