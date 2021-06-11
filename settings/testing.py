import os

from .base import *

TESTING = True

SQLALCHEMY_DATABASE_URI = os.getenv("TEST_DATABASE_URL") or "sqlite://"
