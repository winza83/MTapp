#! /usr/bin/python
from datetime import datetime
def setModeInputGeneral():
	print """
	<option value="0">Train</option>
	<option value="1">Tram</option>
	<option value="2">Bus</option>
	<option value="3">V/Line train or coach</option>
	<option value="4">Nightrider</option>
	"""

def setModeInputPOI():
	setModeInputGeneral()
	print """ <option value="100">Ticket outlet</option> """

def onesetLatLngInput():
	print """
	<fieldset id="one">
	lat: <input type="text" id="lat1" name="lat1" />
	lng: <input type="text" id="lng1" name="lng1" />
	</fieldset>
	"""

def setMethodInput():
	print """
	<select name="methods" OnChange="changeFields(this.selectedIndex)">
	<option value="stopsNearBy">Stops Near By</option>
	<option value="search">Search By Address</option>
	<option value="POI">Search Points of Interest</option>
	<option value="BND">Broad Next Departures</option>
	<option value="SND">Specific Next Departures</option>
	<option value="stoppingPattern">Stopping Pattern</option>
	<option value="stopsOnLine">Stops on Line</option>
	</select>
	"""

def setLimitInput():
	print "<tr><td>limit:</td><td> <input type='number' id='limit' name='limit' value='1' /></td></tr>"


def twosearchByAddress():
	print """
	<fieldset id="two">
	address: <input type="text" width="100" id="searchstr" name="searchstr" />
	</fieldset>
	"""

def threePOI():
	print """
	<fieldset id="three">
	<table>
	<tr><td>lat1:</td><td> <input type="text" id="x1" name="x1" /></td><td>transport type:</td></tr>
	<tr><td>lng1:</td><td> <input type="text" id="y1" name="y1" /></td>
	<td rowspan="6"><select size="6" name="pois" id="pois" multiple>
	"""
	setModeInputPOI()
	print """
	</select></td>
	</tr>
	<tr><td>lat2:</td><td> <input type="text" id="x2" name="x2" /></td></tr>
	<tr><td>lng2:</td><td> <input type="text" id="y2" name="y2" /></td></tr>
	<tr><td>grid depth:</td><td> <input type=number" id="griddepth" name="griddepth" value="1" /></td></tr>
	"""
	setLimitInput()
	print """
	</table>
	</fieldset>
	"""

def setInputContainer():
	print """
	<form id="API" method="POST" action="PTVtestUI.py" onSubmit="loadSession();">
	"""
	setMethodInput()
	onesetLatLngInput()
	twosearchByAddress()
	threePOI()
	fourBND()
	fiveSND()
	print """
	<input type="submit" />
	</form>
	"""

def fourBND():
	print "<fieldset id='four'>"
	print "transport type:<br /> <select size='6' name='poisND' id='poisND'>"
	setModeInputGeneral()
	print '</select><br />'
	print "stop: "
	setStopInput()
	print '<br />'
	setLimitInput()
	print "</fieldset>"

def	setStopInput():
	print "<input id='stop' name='stop' type='text' value='1108' />"

def output():
	print """
	<textarea id="results" cols="100" rows="40">
	</textarea>
	"""

def reqStr():
	print "<textarea id='request' cols='100' rows='5'></textarea>"

def mapBlock():
	print "<div id='mapdiv'></div>"

def setLayout():
	print """<div id="container">"""
	setInputContainer()
	mapBlock()
	reqStr()
	print "</div>"
	output()

def fiveSND():
	print "<fieldset id = 'five'>"
	print "transport type:<br /> <select size='6' name='poiSND' id='poiSND'>"
	setModeInputGeneral()
	print "</select><br />"
	print "line id: "
	print "<input type='number' id='lineid', name='lineid', value='1' /><br /> "
	print "stop id: "
	setStopInput()
	print "direction id: <input type='number' id='directionid', name='directionid', value='1' /><br /> "
	setLimitInput()
	currenttime = (datetime.utcnow().isoformat('T'))[0:19] + 'Z'
	print "for utc: <input type='text' id='time' name='time' value='" + currenttime + "' /><br /> "
	print "</fieldset>"