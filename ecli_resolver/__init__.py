import os

from flask import Flask

# create and configure the app
app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='dev',
)

app.config.from_pyfile('config.py', silent=True)

# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

import ecli_resolver.routes
