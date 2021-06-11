import os

from .base import *

DEBUG = True

SQLALCHEMY_DATABASE_URI = (
    os.getenv("DEV_DATABASE_URL") or f"sqlite:///{BASE_DIR / 'dev.db'}"
)
