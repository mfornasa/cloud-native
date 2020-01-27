from flask import Flask
from config import Config
from flask_pymongo import PyMongo
import sys, logging, json_logging

app = Flask(__name__)
app.config.from_object(Config)
mongo = PyMongo(app)

json_logging.ENABLE_JSON_LOGGING = True
json_logging.init_flask()
json_logging.init_request_instrument(app)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler(sys.stdout))

from app import routes
