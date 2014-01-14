import facebook
import urllib
import urllib2
import json
import urlparse
from flask import render_template,request
from app import engfordev,mongo 

@engfordev.route('/')
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

@engfordev.route('/tag/<string:tag_name>',methods=["GET"])
def tag(tag_name):
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
