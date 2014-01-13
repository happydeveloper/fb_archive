#!/usr/bin/env python
import imp
import os
import sys
import facebook
import urllib
import json
import urllib2
import config
import urlparse
from flask import Flask,render_template,request
from flask.ext.pymongo import PyMongo
import config
import sys, logging

logging.basicConfig(stream=sys.stderr)

myapp = Flask(__name__,static_folder='public/static')
myapp.config["MONGO_HOST"] = config.MONGO_HOST
myapp.config["MONGO_PORT"] = config.MONGO_PORT
myapp.config["MONGO_DBNAME"] = config.MONGO_DBNAME
myapp.config["MONGO_USERNAME"] = config.MONGO_USERNAME
myapp.config["MONGO_PASSWORD"] = config.MONGO_PASSWORD
mongo = PyMongo(myapp)

@myapp.template_filter('urlencode')
def urlencode(uri, **query):
	print uri.encode('utf8')
	parts = list(urlparse.urlparse(uri))
	q = urlparse.parse_qs(parts[4])
	q.update(query)
	parts[4] = urllib.urlencode(q)
	return urlparse.urlunparse(parts)
myapp.jinja_env.globals['urlencode'] = urlencode

@myapp.route('/')
def index():
	col = mongo.db.feed
	hashtags = col.find({"hashtags":{"$exists":True}},{"hashtags":1})
	post = col.find().limit(50)
	tags = {}
	for r in hashtags:
		for t in r["hashtags"]:
			if t in tags:
				tags[t] += 1
			else:
				tags.update({t:1})
	return render_template("index.html",tags=tags,post=post)

@myapp.route('/tag/<string:tag_name>',methods=["GET"])
def tag(tag_name):
	print tag_name
	col = mongo.db.feed
	hashtags = col.find({"hashtags":{"$exists":True}},{"hashtags":1})
	post = col.find({'hashtags':tag_name})
	tags = {}
	for r in hashtags:
		for t in r["hashtags"]:
			if t in tags:
				tags[t] += 1
			else:
				tags.update({t:1})
	return render_template("index.html",tags=tags,post=post)

PYCART_DIR = ''.join(['python-', '.'.join(map(str, sys.version_info[:2]))])

try:
   zvirtenv = os.path.join(os.environ['OPENSHIFT_HOMEDIR'], PYCART_DIR,
                           'virtenv', 'bin', 'activate_this.py')
   execfile(zvirtenv, dict(__file__ = zvirtenv) )
except IOError:
   pass


def run_gevent_server(app, ip, port=8080):
   from gevent.pywsgi import WSGIServer
   WSGIServer((ip, port), app).serve_forever()


def run_simple_httpd_server(app, ip, port=8080):
   from wsgiref.simple_server import make_server
   make_server(ip, port, app).serve_forever()

#
# IMPORTANT: Put any additional includes below this line.  If placed above this
# line, it's possible required libraries won't be in your searchable path
#


#
#  main():
#
if __name__ == '__main__':
	#myapp.run()
	ip   = os.environ['OPENSHIFT_PYTHON_IP']
	port = 8080
	zapp = imp.load_source('application', 'wsgi/application')
	#  Use gevent if we have it, otherwise run a simple httpd server.
	print 'Starting WSGIServer on %s:%d ... ' % (ip, port)
	try:
		run_gevent_server(myapp, ip, port)
	except:
		print 'gevent probably not installed - using default simple server ...'
		run_simple_httpd_server(zapp.application, ip, port)
