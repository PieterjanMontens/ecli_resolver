import os

from flask import Flask
from ecli_resolver.util import ECLIConverter
from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'DEBUG',
        'handlers': ['wsgi']
    }
})

# create and configure the app
app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='dev',
)

app.config.from_pyfile('config.py', silent=True)
app.url_map.converters['ecli'] = ECLIConverter

# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

import ecli_resolver.routes
