import os

from .base import *

DEBUG = False
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
