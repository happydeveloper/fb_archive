#!/usr/bin/env python
import imp
import os
import sys
import facebook
import urllib
import json
import urllib2
from flask import Flask

myapp.debug = True
myapp = Flask(__name__)

@myapp.route('/')
def hello_world():
    return "Hello World!"

@myapp.route('/get_access_token')
def get_access_token():
	app_id = "626851570705028"
	app_secret = "aba7af8db27670642efb196ab968ce42"
	group_id = "157076174344216"
	token = facebook.get_app_access_token(app_id,app_secret)
	response = urllib2.urlopen("https://graph.facebook.com/" + group_id + "?fields=feed&method=GET&format=json&suppress_http_code=1&access_token=" + str(token))
	feed = json.loads(response.read())
	return feed


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
