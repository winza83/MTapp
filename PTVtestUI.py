#! /usr/bin/python
import PTVfactory as P
import cgi
import cgitb
import layout
cgitb.enable()

form = cgi.FieldStorage()

googleKey = 'AIzaSyDejfQWInSUrLPFX8iTFQ0fBm62RdKPLNo'
baseurl = "http://timetableapi.ptv.vic.gov.au"
key = '29246674-a96c-11e3-8bed-0263a9d0b8a0'
devid = 1000050
test = P.Trans(googleKey, key, devid)

print "Content-type: text/html \n"
print "<!DOCTYPE html>"
print "<head>"
print "<title>PTV test harness</title>"
print """
	<link rel="stylesheet" href="styles.css" type="text/css" />
	<title>Testing PTV API</title>
	<script type="text/javascript" src="jquery/jquery-2.0.3.js"></script>
	<script type="text/javascript" src="http://maps.google.com/maps/api/js?sensor=false&libraries=drawing"></script>
	<script type="text/javascript">
		var drawman = new google.maps.drawing.DrawingManager({
			drawingControl: true,
		 	drawingControlOptions: {drawingModes: [google.maps.drawing.OverlayType.RECTANGLE]}
			});
		var map = [];
		function initialize() {
		    var myOptions = {
				center:  new google.maps.LatLng(-37.85, 145.05),
				zoom: 9,
				mapTypeId: google.maps.MapTypeId.ROADMAP
			};
			map[0] = new google.maps.Map(document.getElementById("mapdiv"), myOptions);

			google.maps.event.addListener(map[0], 'click', function(event) {
				if (typeof(marker) !== "undefined")  {
					for (var i = 0; i < marker.length; i++)
						marker[i].setMap(null);
				}
				var choice = document.getElementsByName("methods")[0].value;
				switch (choice) {
					case 'stopsNearBy':
						poi = event.latLng;
						document.getElementById('lat1').value = poi.lat();
						document.getElementById('lng1').value = poi.lng();
						marker = [];
						marker[marker.length] = new google.maps.Marker({icon: 'pt.png', position: poi, map: map[0]});
					case 'POI':
						break;
					}

				}
			);

			google.maps.event.addListener(drawman, 'rectanglecomplete', function(event) {
			  if (event.type == google.maps.RECTANGLE) {
				var y2 = event.getBounds().getNorthEast().lat();
				var x2 = event.getBounds().getNorthEast().lng();
				var y1 = event.getBounds().getSouthWest().lat();
				var x1 = event.getBounds().getSouthWest().lng();

				document.getElementById("x1").value = x1;
				document.getElementById("x2").value = x2;
				document.getElementById("y1").value = y1;
				document.getElementById("y2").value = y2;
			  }
			});
		}

		function startUp() {
			if (sessionStorage.length != 0) {
				initialize();
				getData();
			}
			else {
				initialize();
			}
		}

		function changeFields(selection) {
			var mapobj = map[0];
			map[0] = mapobj;
			drawman.setMap(null);
			var box = document.getElementsByTagName('fieldset');
			for (i = 0; i < box.length; i++) {
				if (i == parseInt(selection)) {
					box[i].style.display = "block";
				}
				else {
					box[i].style.display = "none";
				}
			}
			if (document.getElementsByName("methods")[0].value == 'POI') {
					drawman.setMap(mapobj);
			}
		}

		function loadSession() {
			sessionStorage.setItem('marker',1);
		}


	function getData() {
		if (sessionStorage.length > 0) {

"""
if form.getvalue('methods') == 'stopsNearBy':
	latitude, longitude = str(form.getvalue('lat1')), str(form.getvalue('lng1'))
	reqstr = test.delegator('stopsNearBy', [latitude, longitude])
elif form.getvalue('methods') == 'search':
	searchstr = str(form.getvalue('searchstr'))
	reqstr = test.delegator('search', [searchstr])
elif form.getvalue('methods') == 'POI':
	lat1, lng1, lat2, lng2 = form.getvalue("y2"), form.getvalue("x1"), form.getvalue("y1"), form.getvalue("x2")
	griddepth, limit, poi = form.getvalue("griddepth"), form.getvalue("limit"), form.getvalue("pois")
	reqstr = test.delegator('POI', [poi, lat1, lng1, lat2, lng2, griddepth, limit])
elif form.getvalue('methods') == 'BND':
	mode, stop, limit = form.getvalue('poisND'), form.getvalue('stop'), (form.getvalue('limit'))[1]	#1st elem because it is the second limit input field
	reqstr = test.delegator('BND', [mode, stop, limit])

if ('reqstr' in locals() or 'reqstr' in globals()) and len(reqstr) > 0:
	print "document.getElementById('request').innerHTML = '" + reqstr + "';"
	data = test.getData(reqstr)
	pretty = (str(data.encode('utf-8'))).replace("\n","\\n")
	print "document.getElementById('results').value = '" + pretty +"';"
print """
		}
	}

	</script>
	</head>
	<body onload="startUp()">
"""
layout.setLayout()
print "</body></html>"
