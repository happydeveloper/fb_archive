#!/usr/bin/env python
import urllib2
import config
import json
import facebook

token = config.ACCESS_TOKEN
response = urllib2.urlopen("https://graph.facebook.com/" + config.GROUPS["engfordev"] + "?fields=feed&method=GET&format=json&suppress_http_code=1&access_token=" + str(token))
data = json.loads(response.read())
articles = []
print data
'''
feed = data["feed"]
for f in feed["data"]:
	comment = []
	if "comments" in f:
		for c in f["comments"]["data"]:
			comment.append({"name":c["from"]["name"],"message":c["message"]})
	articles.append({"name":f["from"]["name"],"message":f["message"],"comment":comment})

print articles
'''
