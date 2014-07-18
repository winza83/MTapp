#!/usr/bin/python2.7
import hmac
import urllib as url
import json

import cgi
import cgitb
import json
import urllib2 as url
import unicodedata

cgitb.enable()

data = url.urlopen('http://services.land.vic.gov.au/catalogue/publicproxy/guest/sdm_geoserver/wfs?request=GetFeature&typename=sii:RAEDATA.DPS_932_RAIL_STATIONS_VMT&outputformat=application/json');

file = open("trainstation.json","w");

file.writelines(data.read())
file.close()
print "Content-type: text/html"

print """
<html>
  <head>
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
    <meta charset="utf-8">
    <title>Ground Overlays</title>
    <style>
      html, body {
        height: 100%;
        margin: 0px;
        padding: 0px
      }

       #map-canvas {
		height: 80%;
       }
    </style>
    <script src="https://maps.googleapis.com/maps/api/js?v=3.exp&sensor=false"></script>
    <script src="http://www.openlayers.org/api/OpenLayers.js"></script>
	<script src="geoxml3.js"></script>
	<script src="ProjectedOverlay.js"></script>
    <script>

var ov;

function initialize() {

  var origin = new google.maps.LatLng(-37.826301, 144.969178);
  var mapOptions = {
    zoom: 16,
    center: origin
  };

  var map = new google.maps.Map(document.getElementById('map-canvas'),
      mapOptions);


var myParser = new geoXML3.parser({map: map, zoom: false});
myParser.parse('http://124.190.54.81/MTApp/KML_BUS_DATA.kml');

var tramroutes = new google.maps.KmlLayer({
    url: 'http://services.land.vic.gov.au/catalogue/publicproxy/guest/sdm_geoserver/wms?SERVICE=WMS&VERSION=1.1.1&REQUEST=GetMap&WIDTH=512&HEIGHT=512&LAYERS=sii%3ARAEDATA.DPS_969_TRAM_ROUTES_VMT&STYLES=&FORMAT=kml&SRS=EPSG%3A4283&BBOX=144.50%2C-38.49%2C145.70%2C-37.45'
  });

var trainlines1 = new google.maps.KmlLayer({url: 'http://services.land.vic.gov.au/catalogue/publicproxy/guest/sdm_geoserver/wms?SERVICE=WMS&VERSION=1.1.1&REQUEST=GetMap&WIDTH=300&HEIGHT=100&LAYERS=sii%3ARAEDATA.DPS_1202_TRAIN_CORR_CENTL&STYLES=&FORMAT=kml&SRS=EPSG%3A4283&BBOX=144.501%2C-38.49%2C145.7%2C-37.45'});

trainlines1.setMap(map);

"""
data = json.load(url.urlopen('http://124.190.54.81/MTApp/trainstation.json'));


print "var markerarray = [];"

for i in data['features']:
	print "var lat = " + str(i['geometry']['coordinates'][0]) + ";"
	print "var lng = " + str(i['geometry']['coordinates'][1]) + ";"
	print "markerarray.push(new google.maps.Marker({position: new google.maps.LatLng(lat,lng), map: map, icon: 'train.png' }));"

print """
for (i = 0; i < markerarray.length; i++) {
	markerarray[i].setMap(map);
	}
}
"""
print """
google.maps.event.addDomListener(window, 'load', initialize);
    </script>
  </head>
  <body>
    <div id="map-canvas"></div>
  </body>
</html>
"""






