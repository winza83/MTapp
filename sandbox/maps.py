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
			});
		}

		function addMarker() {
			marker = new google.maps.Marker({
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
			marker.setMap(null);
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

