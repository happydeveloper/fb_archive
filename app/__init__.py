import config
from flask import Flask
from flask.ext.pymongo import PyMongo

engfordev = Flask(__name__,static_folder='../public/static')
engfordev.config["MONGO_HOST"] = config.MONGO_HOST
engfordev.config["MONGO_PORT"] = config.MONGO_PORT
engfordev.config["MONGO_DBNAME"] = config.MONGO_DBNAME
engfordev.config["MONGO_USERNAME"] = config.MONGO_USERNAME
engfordev.config["MONGO_PASSWORD"] = config.MONGO_PASSWORD
mongo = PyMongo(engfordev)

import views
