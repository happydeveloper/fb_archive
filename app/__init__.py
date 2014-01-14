import config
from flask import Flask
from flask.ext.pymongo import PyMongo

myapp = Flask(__name__,static_folder='../public/static')
myapp.config["MONGO_HOST"] = config.MONGO_HOST
myapp.config["MONGO_PORT"] = config.MONGO_PORT
myapp.config["MONGO_DBNAME"] = config.MONGO_DBNAME
myapp.config["MONGO_USERNAME"] = config.MONGO_USERNAME
myapp.config["MONGO_PASSWORD"] = config.MONGO_PASSWORD
mongo = PyMongo(myapp)

import views
