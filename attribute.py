#! /usr/bin/python
import cgi
import cgitb
cgitb.enable()

def plotDraw():
	print """
	markers = []
	function plotMap(transtype, lat, lng) {
		icon = '';

		if (transtype == "nightrider" || transtype == "bus") {
			icon = 'bus.png';
		}
		else if (transtype == "tram") {
			icon = 'tram.png';
			}
		else if (transtype == "train") {
			icon = 'train.png';
		}
		else {
			icon = 'shop.png';
		}

		var image = {
		url: icon,
		size: new google.maps.Size(20, 20),
		origin: new google.maps.Point(0, 0),
		anchor: new google.maps.Point(0, 0),
		scaledSize: new google.maps.Size(20,20)
		};

		markers.push(new google.maps.Marker({
			position: new google.maps.LatLng(lat, lng),
			icon: image
		}));
		markers[markers.length - 1].setMap(map[0]);
	}
	"""

def iteratePOI():
	print """
	function iteratePOI(obj) {
	for (i = 0; i < data['locations'].length; i++) {
		result = data['locations'][i];
		lat = result['lat'];
		lng = result['lon'];
		locationame = result['location_name'];
		stopid = result['stop_id'];
		suburb = result['suburb'];
		transtype = result['transport_type'];
		if (result['outlet_type']) {
			businessname = result['business_name'];
			outlettype = result['outlet_type'];
			transtype = result['outlet_type'];
		}
		plotMap(transtype, lat, lng);
		}
	}

	"""

def stopsNearBy():
	print """
	data = JSON.parse(document.getElementById('results').value);

	markers = []
	for (i = 0; i < data.length; i++) {
		result = data[i]['result'];
		lat = result['lat'];
		lng = result['lon'];
		transtype = data[i]['result']['transport_type'];
		plotMap(transtype, lat, lng);
	}
	reqtext = document.getElementById('request').value;
	temp = reqtext.substring(reqtext.search("latitude"), reqtext.search("devid") - 1);
	temp2 = temp.replace("/longitude/", ",");
	latlng = (temp2.replace("latitude/", "")).split(",");
	origin = new google.maps.LatLng(parseFloat(latlng[0]), parseFloat(latlng[1]));
	originMarker = new google.maps.Marker({
		position: origin,
		icon: 'pt.png'});
	originMarker.setMap(map[0]);
	map[0].setCenter(origin);
	map[0].setZoom(13);
	"""

def plotPOI():
	print """
	data = JSON.parse(document.getElementById('results').value);
	markers = []
	if (data['clusters']) {
		if (data['locations']) {
			iteratePOI(data['clusters']);
			}
		}
	else if (data['locations']) {
		if (data['clusters']) {
			iteratePOI(data['locations']);
			}
		}

	"""

def plotStopsLine():
	print """
	data = JSON.parse(document.getElementById('results').value);
	markers = []
	for (i = 0; i < data.length; i++) {
		lat = data[i]['lat'];
		lng = data[i]['lon'];
		stname = data[i]['location_name'];
		transtype = data[i]['transport_type'];
		plotMap(transtype, lat, lng);
	}
	"""


def map(methods):
	plotDraw()
	iteratePOI()
	if methods == 'stopsNearBy' or methods == 'search':
		stopsNearBy()
	elif methods == 'POI':
		plotPOI()
	elif methods == 'stopsOnLine':
		plotStopsLine()
"""

snb, search address
stops nearby
data[0]['type']
data[0]['result']
data[0]['result']['distance']
data[0]['result']['location_name']
data[0]['result']['lat']
data[0]['result']['long']
data[0]['result']['stop_id']
data[0]['result']['suburb']
data[0]['result']['transport_type']

poi
data['minLong']
data['maxLong']
data['minLat']
data['maxLat']
data['weightedLong']
data['weightedLat']
data['totalLocations']
data['clusters']
data['locations'][0]
data['locations'][0]['distance']
data['locations'][0]['location_name']
data['locations'][0]['lat']
data['locations'][0]['lon']
data['locations'][0]['stop_id']
data['locations'][0]['suburb']
data['locations'][0]['transport_type']

bnd, snd, stoppingpattern
data['values']
data['values'][0]['platform']
data['values'][0]['platform']['realtime_id']
data['values'][0]['platform']['stop']
data['values'][0]['platform']['stop']['distance']
data['values'][0]['platform']['stop']['location_name']
data['values'][0]['platform']['stop']['lat']
data['values'][0]['platform']['stop']['lon']
data['values'][0]['platform']['stop']['suburb']
data['values'][0]['platform']['stop']['stop_id']
data['values'][0]['platform']['stop']['transport_type']
data['values'][0]['platform']['direction']
data['values'][0]['platform']['direction']['direction_id']
data['values'][0]['platform']['direction']['direction_name']
data['values'][0]['platform']['direction']['linedir_id']
data['values'][0]['platform']['direction']['line']
data['values'][0]['platform']['direction']['line']['line_id']
data['values'][0]['platform']['direction']['line']['transport_type']
data['values'][0]['platform']['direction']['line']['line_name']
data['values'][0]['platform']['direction']['line']['line_number']
data['values'][0]['platform']['direction']['line']
data['values'][0]['run']
data['values'][0]['run']['destination_id']
data['values'][0]['run']['destination_name']
data['values'][0]['run']['transport_type']
data['values'][0]['run']['num_skipped']
data['values'][0]['run']['run_id']
data['values'][0]['flags']
data['values'][0]['time_timetable_utc']
data['values'][0]['time_realtime_utc']

stops on line
data[0]['distance']
data[0]['location_name']
data[0]['lat']
data[0]['lon']
data[0]['suburb']
data[0]['transport_type']
data[0]['stop_id']

"""