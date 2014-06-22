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

#js = json.load(data)

#unicode(js).encode('ascii','ignore')

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
// This example uses a GroundOverlay to place an image on the map
// showing an antique map of origin, NJ.

var ov;

function initialize() {
//open layers stuff
  //-37.85, 145.05
//  var imageBounds = new google.maps.LatLngBounds(
  //    new google.maps.LatLng(-38.49, 144.50),
    //  new google.maps.LatLng(-37.45, 145.70));
  var origin = new google.maps.LatLng(-37.826301, 144.969178);
  var mapOptions = {
    zoom: 16,
    center: origin
  };

  var map = new google.maps.Map(document.getElementById('map-canvas'),
      mapOptions);
//BBOX=143.501%2C-38.60%2C148.068%2C-37.01
//WIDTH=3000&HEIGHT=1125
//http://services.land.vic.gov.au/catalogue/publicproxy/guest/sdm_geoserver/wms?SERVICE=WMS&VERSION=1.1.1&REQUEST=GetMap&WIDTH=3000&HEIGHT=1472&LAYERS=sii%3ARAEDATA.DPS_955_METRO_BUS_ROUTES&STYLES=&FORMAT=image%2Fpng&SRS=EPSG%3A4283&BBOX=143.501%2C-38.60%2C148.068%2C-37.01
//http://services.land.vic.gov.au/catalogue/publicproxy/guest/sdm_geoserver/wms?SERVICE=WMS&VERSION=1.1.1&REQUEST=GetMap&WIDTH=3000&HEIGHT=1472&LAYERS=sii%3ARAEDATA.DPS_955_METRO_BUS_ROUTES&STYLES=&FORMAT=image%2Fpng&SRS=EPSG%3A4283&BBOX=143.501%2C-38.60%2C148.068%2C-37.01
//  ov = new google.maps.GroundOverlay(
 //     'http://services.land.vic.gov.au/catalogue/publicproxy/guest/sdm_geoserver/wms?SERVICE=WMS&VERSION=1.1.1&REQUEST=GetMap&WIDTH=3000&HEIGHT=2600&LAYERS=sii%3ARAEDATA.DPS_955_METRO_BUS_ROUTES&STYLES=&FORMAT=image%2Fpng&transparent=true&SRS=EPSG%3A4283&BBOX=144.50%2C-38.49%2C145.70%2C-37.45&isBaseLayer=false',
 //     imageBounds);
//  ov.setMap(map);

var myParser = new geoXML3.parser({map: map, zoom: false});
//myParser.parse('http://localhost/meh/MTapp/data/KML_BUS_DATA.kml');
//myParser.parseKmlString("<Placemark><LineString><coordinates>145.06049199999995,-37.85999503715753 145.059707,-37.860018037157545 145.05954699999995,-37.86002403715754 145.05942200000004,-37.86002203715754 145.059343,-37.86003003715752 145.05926300000002,-37.86002803715752 145.059036,-37.86003403715753 145.05892200000005,-37.86004103715757 145.05895899999996,-37.85991503715741 145.05884600000002,-37.85945403715698 145.05863499999998,-37.85927903715678</coordinates></LineString></Placemark>");
var tramroutes = new google.maps.KmlLayer({
    url: 'http://services.land.vic.gov.au/catalogue/publicproxy/guest/sdm_geoserver/wms?SERVICE=WMS&VERSION=1.1.1&REQUEST=GetMap&WIDTH=512&HEIGHT=512&LAYERS=sii%3ARAEDATA.DPS_969_TRAM_ROUTES_VMT&STYLES=&FORMAT=kml&SRS=EPSG%3A4283&BBOX=144.50%2C-38.49%2C145.70%2C-37.45'
  });

//myParser.parse('http://localhost/meh/MTapp/newtrainlines.kml');

var trainlines1 = new google.maps.KmlLayer({url: 'http://services.land.vic.gov.au/catalogue/publicproxy/guest/sdm_geoserver/wms?SERVICE=WMS&VERSION=1.1.1&REQUEST=GetMap&WIDTH=300&HEIGHT=100&LAYERS=sii%3ARAEDATA.DPS_1202_TRAIN_CORR_CENTL&STYLES=&FORMAT=kml&SRS=EPSG%3A4283&BBOX=144.501%2C-38.49%2C145.7%2C-37.45'});


//tramroutes.setMap(map);
trainlines1.setMap(map);
//trainlines2.setMap(map);
//trainlines3.setMap(map);
//trainlines4.setMap(map);
"""



print "map.data.loadGeoJson('http://localhost/meh/MTapp/trainstation.json');"

print """
  	map.setZoom(8);

}

google.maps.event.addDomListener(window, 'load', initialize);

    </script>
  </head>
  <body>
    <div id="map-canvas"></div>
  </body>
</html>
"""






