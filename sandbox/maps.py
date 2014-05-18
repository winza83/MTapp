#!/usr/bin/python
import cgi
import cgitb

cgitb.enable()


print "Content-type: text/html"
print """
<!--WSO - 17/5/2014 Simple web page to test the capabiltiies of GME -->
<!DOCTYPE html>
	<head>
		<style type="text/css">
		#mapdiv {
			height:500px;
			width:1000px;
			margin: 0 auto;
		}
		</style>
		<script type="text/javascript" src="http://maps.google.com/maps/api/js?sensor=false"></script>

		<script type="text/javascript">
		i = 0;
  		function initialize() {
		    var myOptions = {
				center:  new google.maps.LatLng(-37.85, 145.05),
				zoom: 9,
				mapTypeId: google.maps.MapTypeId.ROADMAP
			};

			map = new google.maps.Map(document.getElementById("mapdiv"), myOptions);

			google.maps.event.addListener(map, 'click', function(event) {
				poi = event.latLng;
				document.getElementById("value").innerHTML=poi;
				document.getElementById("coord").value=poi;
				document.getElementById("tog").disabled=false;
				if (i == 1) {
					removeMarker();
					addMarker();
				}
			});

			markers = new Array();

			if (sessionStorage.length != 0) {
				var data = (sessionStorage.getItem('results'));
				var results = data.split(",");

				for (var j = 0; j < results.length; j++) {
					record = results[j].replace("(","");
					record = results[j].replace(")","")
//					document.getElementById("value").innerHTML=record;
					row = record.split("|");
					poi = new google.maps.LatLng(row[1], row[2]);
					if (j == 0) {
						origin = poi;
					}
					document.getElementById("value").innerHTML=poi;
					markers[j] = new google.maps.Marker({position: poi, map: map});
					markers[j].setMap(map);
				}
				i = 1;
				map.setCenter(origin);
				map.setZoom(14);
			}
		}

		function addMarker() {
			sessionStorage.clear();
			markers[markers.length] = new google.maps.Marker({
				position: poi,
				map: map
			});
			i = 1;
		}


		function toggle() {
			if (i == 0) {
				addMarker();
			}
			else {
				removeMarker();
			}
		}

		function removeMarker() {
			for (j = 0; j < markers.length; j++) {
				markers[j].setMap(null);
			}
			i = 0;
		}


</script>
</head>
<body onload="initialize()">
  <div id="mapdiv">werwr</div>
  <p id="value"> </p>
  <input id="tog" type="button" value="toggle marker" disabled="disabled" onClick="toggle()" />
  <form id="test" method="post" action="test.py" >
  <input id="enter" type="submit" />
  <input id="coord" name="coord" type="hidden" value="" />
  </form>
</body>
<!-- notes
-37.85, 145.05
-37, 144
-38, 146
need to refer to http://stevage.github.io/PTV-API-doc/#header1
-->
</html>
"""

