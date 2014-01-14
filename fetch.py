#!/usr/bin/env python
import urllib2
import config
import json
import facebook
import time
import re
from pymongo import MongoClient
conn = "mongodb://" + config.MONGO_USERNAME + ":" + config.MONGO_PASSWORD + "@" + config.MONGO_HOST + ":" + config.MONGO_PORT + "/" + config.MONGO_DBNAME
client = MongoClient(conn)
token = config.ACCESS_TOKEN
response = urllib2.urlopen("https://graph.facebook.com/" + config.GROUPS["engfordev"] + "?fields=feed&method=GET&format=json&suppress_http_code=1&access_token=" + str(token))
data = json.loads(response.read())

if "error" in data:
	if data["error"]["code"] == 613:
		time.sleep(600)
		response = urllib2.urlopen("https://graph.facebook.com/" + config.GROUPS["engfordev"] + "?fields=feed&method=GET&format=json&suppress_http_code=1&access_token=" + str(token))
		data = json.loads(response.read())

prev = data["feed"]["paging"]["next"]
feed = data["feed"]
col = #MONGO DB COLLECTION
col.drop()
col.insert(feed["data"])
total_request = 1
while prev:
	total_request += 1
	try:
		response = urllib2.urlopen(prev)
		data = json.loads(response.read())
		if len(data["data"]) > 0:
			col.insert(data["data"])
		if "paging" in data and "next" in data["paging"]:
			prev = data["paging"]["next"]
		else:
			prev = False
	except urllib2.HTTPError:
		print "Request error: [Url:" + prev + "]\n"
		time.sleep(60)

print "Total Request: [" + str(total_request) + "]"

feed = col.find()
hash_reg = re.compile("\s[#]\S+",re.UNICODE)
for f in feed:
	tags = []
	if "message" in f:
		filtered_tags = hash_reg.findall(f["message"])
		if len(filtered_tags) > 0:
			for t in filtered_tags:
				tags.append(t.strip())
	if "comments" in f:
		for c in f["comments"]["data"]:
			filtered_tags = hash_reg.findall(c["message"])
			if len(filtered_tags) > 0:
				for t in filtered_tags:
					tags.append(t.strip())
	if len(tags) > 0:
		col.update({"_id":f["_id"]},{'$set':{"hashtags":tags}},upsert=True)
