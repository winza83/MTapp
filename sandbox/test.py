#!/usr/bin/python2.7
import hmac
import urllib as url
import json

import cgi
import cgitb
from hashlib import sha1
#import requests
cgitb.enable()
print "Content-type: text/html"
print
print "<html><title>testpg</title>"
form = cgi.FieldStorage()
try:
	coord = form.getvalue("coord")
except:
	pass

coord = coord[1:-1]
print coord
i = 0
print "<script type='text/Javascript'>"


key = '29246674-a96c-11e3-8bed-0263a9d0b8a0'
h = hmac.new(key,'',sha1)
baseurl = "http://timetableapi.ptv.vic.gov.au"
devid=1000050
lat =float(coord.split(",")[0])
lng =float(coord.split(",")[1])
request = "/v2/nearme/latitude/" + str(lat) + "/longitude/" + str(lng)
h.update(request + "?devid=" + str(devid))
signature = h.hexdigest().upper()
#print request

#print signature
str1 = baseurl + request + "?devid=" + str(devid) +"&signature=" + signature
#print str1
result1 = url.urlopen(str1)
doc = result1.read()
jdata = json.loads(doc)

i = 0
print "var data = new Array();"
print "data.push('" + "origin|" + str(lat) + "|" + str(lng) + "');"
for record in jdata:
	loc = jdata[i]["result"]["location_name"]
	lat = jdata[i]["result"]["lat"]
	lng = jdata[i]["result"]["lon"]
	row = "'(" + str(loc) + "|" + str(lat) + "|" + str(lng) + ")'"
	print "data.push(" + row + ");"
	i = i + 1

print "sessionStorage.setItem('results',data);"
print """
	window.location = 'maps.py';
"""
#requests.post("http://timetableapi.ptv.vic.gov.au/v2/nearme/latitude/-37.817993/longitude/144.981916?devid=1000050&signature=A5F275F27B40D41A9B140671FFEED886D34FDDD1")
#def getUrl(request):
#	pass

#def getsignature(request):
#	h = hmac.new(key,'',sha1)
#	h.update(request)
#	return h.hexdigest()

#http://timetableapi.ptv.vic.gov.au/v2/nearme/latitude/-37.817993/longitude/144.981916?devid=1000050&signature=A5F275F27B40D41A9B140671FFEED886D34FDDD1
#http://timetableapi.ptv.vic.gov.au/v2/nearme/latitude/-37.817993/longitude/144.981916?devid=1000050&signature=a5f275f27b40d41a9b140671ffeed886d34fddd1
print"</script>"
print "<head>"
print """
</head><body >
"""


print "</body></html>"



