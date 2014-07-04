#! /usr/bin/python
import PTVfactory as P
import cgi
import cgitb
cgitb.enable()

form = cgi.FieldStorage()

googleKey = 'your key here'
baseurl = "http://timetableapi.ptv.vic.gov.au"
key = 'your key here'
devid=your dev id
test = P.Trans('AIzaSyDejfQWInSUrLPFX8iTFQ0fBm62RdKPLNo', '29246674-a96c-11e3-8bed-0263a9d0b8a0', 1000050)

print "Content-type: text/html \n"
print "<!DOCTYPE html>"
print "<head>"
print "<title>PTV test harness</title>"
print """
	<link rel="stylesheet" href="styles.css" type="text/css" />
	<title>Testing PTV API</title>
	<script type="text/javascript" src="http://maps.google.com/maps/api/js?sensor=false"></script>
	<script type="text/javascript">

		function initialize() {
		    var myOptions = {
				center:  new google.maps.LatLng(-37.85, 145.05),
				zoom: 9,
				mapTypeId: google.maps.MapTypeId.ROADMAP
			};

			var map = new google.maps.Map(document.getElementById("mapdiv"), myOptions);
			google.maps.event.addListener(map, 'click', function(event) {
				poi = event.latLng;
				document.getElementById('lat1').value = poi.lat();
				document.getElementById('lng1').value = poi.lng();
				}
			);
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
			var box = document.getElementsByTagName('fieldset');
			for (i = 0; i < box.length; i++) {
				if (i == parseInt(selection)) {
					box[i].style.display = "block";
				}
				else {
					box[i].style.display = "none";
				}
			}
		}

		function loadSession() {
			sessionStorage.setItem('marker',1);
		}


	function getData() {
		if (sessionStorage.length > 0) {

"""
if form.getvalue('methods') == 'stopsnearby':
	print "document.getElementById('lat1').value = " +	str(form.getvalue('lat1')) + ";"
	print "document.getElementById('lng1').value = " +	str(form.getvalue('lng1')) + ";"
	reqstr =  "document.getElementById('request').innerHTML= '" + test.stopsNearBy(form.getvalue('lat1'), form.getvalue('lng1')) + "';"
	data = test.getData((test.stopsNearBy(form.getvalue('lat1'), form.getvalue('lng1'))))
elif form.getvalue('methods') == 'search':
	print "document.getElementById('searchstr').value = '" +	str(form.getvalue('searchstr')) + "';"
	reqstr =  "document.getElementById('request').innerHTML= '" + test.search(form.getvalue('searchstr')) + "';"
	data = test.getData(test.search(form.getvalue('searchstr')))

if 'reqstr' in locals() or 'reqstr' in globals():
	print reqstr
	pretty = (str(data.encode('utf-8'))).replace("\n","\\n")
	print "document.getElementById('results').value = '" + pretty +"';"
print """
		}
	}

	</script>
	</head>
	<body onload="startUp()">
		<div id="mapdiv">
		</div>
		<div id="container">
			<form id="API" method="POST" action="PTVtestUI.py" onSubmit="loadSession();">
				<select name="methods" OnChange="changeFields(this.selectedIndex)">
					<option value="stopsnearby">Stops Near By</option>
					<option value="search">Search By Address</option>
					<option value="POI">Search Points of Interest</option>
					<option value="BND">Broad Next Departures</option>
					<option value="SND">Specific Next Departures</option>
					<option value="StoppingPattern">Stopping Pattern</option>
					<option value="stopsOnLine">Stops on Line</option>
				</select>
				<fieldset id="one">
					<input type="text" id="lat1" name="lat1" />
					<input type="text" id="lng1" name="lng1" />
				</fieldset>
				<fieldset id="two">
					<input type="text" id="searchstr" name="searchstr" />
				</fieldset>
				<input type="submit" />
			</form>
		</div>
		<br />		<br />
		<div id="request">

		</div>
		<textarea id="results" cols="100" rows="100">
		</textarea>

	</body>
	</html>
"""
