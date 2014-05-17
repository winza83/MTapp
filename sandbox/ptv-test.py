#! usr/bin/python
import hmac
import urllib as url
import json
from hashlib import sha1
key = '29246674-a96c-11e3-8bed-0263a9d0b8a0'
h = hmac.new(key,'',sha1)
baseurl = "http://timetableapi.ptv.vic.gov.au"
devid=1000050
lat =-37.845840
lng = 145.265528
request = "/v2/nearme/latitude/" + str(lat) + "/longitude/" + str(lng)
h.update(request + "?devid=" + str(devid))
signature = h.hexdigest().upper()
print request
print ""
print signature
str1 = baseurl + request + "?devid=" + str(devid) +"&signature=" + signature
result1 = url.urlopen(str1)
doc = result1.read()
jdata = json.loads(doc)
jdata[0]["type"]
i = 0
for record in jdata:
	print jdata[i]["result"]["location_name"]
	i = i + 1

#def getUrl(request):
#	pass

#def getsignature(request):
#	h = hmac.new(key,'',sha1)
#	h.update(request)
#	return h.hexdigest()

#http://timetableapi.ptv.vic.gov.au/v2/nearme/latitude/-37.817993/longitude/144.981916?devid=1000050&signature=A5F275F27B40D41A9B140671FFEED886D34FDDD1
#http://timetableapi.ptv.vic.gov.au/v2/nearme/latitude/-37.817993/longitude/144.981916?devid=1000050&signature=a5f275f27b40d41a9b140671ffeed886d34fddd1