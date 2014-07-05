#! /usr/bin/python
import PTVfactory as P
import cgi
import cgitb
cgitb.enable()

form = cgi.FieldStorage()

googleKey = yourgooglekey
key = yourkey
baseurl = "http://timetableapi.ptv.vic.gov.au"
devid = yourdevid
test = P.Trans(googleKey, key, devid)

print "Content-type: text/html \n"
print "<!DOCTYPE html>"
print "<head>"
print "<title>PTV test harness</title>"
print """
	<link rel="stylesheet" href="styles.css" type="text/css" />
	<title>Testing PTV API</title>
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
				alert("here");
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
	lat1 = form.getvalue("y2")
	lng1 = form.getvalue("x1")
	lat2 = form.getvalue("y1")
	lng2 = form.getvalue("x2")
	griddepth = form.getvalue("griddepth")
	limit = form.getvalue("limit")
	poi = form.getvalue("pois")
	reqstr = test.delegator('POI', [poi, lat1, lng1, lat2, lng2, griddepth, limit])

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
		<div id="container">
			<form id="API" method="POST" action="PTVtestUI.py" onSubmit="loadSession();">
				<select name="methods" OnChange="changeFields(this.selectedIndex)">
					<option value="stopsNearBy">Stops Near By</option>
					<option value="search">Search By Address</option>
					<option value="POI">Search Points of Interest</option>
					<option value="BND">Broad Next Departures</option>
					<option value="SND">Specific Next Departures</option>
					<option value="stoppingPattern">Stopping Pattern</option>
					<option value="stopsOnLine">Stops on Line</option>
				</select>
				<fieldset id="one">
					lat: <input type="text" id="lat1" name="lat1" />
					lng: <input type="text" id="lng1" name="lng1" />
				</fieldset>
				<fieldset id="two">
					address: <input type="text" width="100" id="searchstr" name="searchstr" />
				</fieldset>
				<fieldset id="three">
					<table>
					<tr><td>lat1:</td><td> <input type="text" id="x1" name="x1" /></td><td>transport type:</td></tr>
					<tr><td>lng1:</td><td> <input type="text" id="y1" name="y1" /></td>
					<td rowspan="6"><select size="6" name="pois" id="pois" multiple>
							<option value="0">Train</option>
							<option value="1">Tram</option>
							<option value="2">Bus</option>
							<option value="3">V/Line train or coach</option>
							<option value="4">Nightrider</option>
							<option value="100">Ticket outlet</option>
							</select></td></tr>
					<tr><td>lat2:</td><td> <input type="text" id="x2" name="x2" /></td></tr>
					<tr><td>lng2:</td><td> <input type="text" id="y2" name="y2" /></td></tr>
					<tr><td>grid depth:</td><td> <input type=number" id="griddepth" name="griddepth" value="1" /></td></tr>
					<tr><td>limit:</td><td> <input type=number" id="limit" name="limit" value="1" /></td></tr>
					</table>
				</fieldset>
				<input type="submit" />
			</form>
		<div id="mapdiv"></div>
		<textarea id="request" cols="100" rows="5"></textarea>
		</div>

		<textarea id="results" cols="100" rows="85">
		</textarea>

	</body>
	</html>
"""
