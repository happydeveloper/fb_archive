import facebook
import json
import urlparse
from collections import OrderedDict
from operator import itemgetter
from flask import render_template,request
from app import myapp,mongo
import filters

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
	tags = OrderedDict(sorted(tags.items(), key=itemgetter(1),reverse=True))
	return render_template("index.html",tags=tags,post=post)

@myapp.route('/tag/<string:tag_name>',methods=["GET"])
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
	tags = OrderedDict(sorted(tags.items(), key=itemgetter(1),reverse=True))
	return render_template("index.html",tags=tags,post=post)
