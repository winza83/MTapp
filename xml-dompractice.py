#! usr/bin/python
""""
import xml.dom.minidom as mini

docs = open("wms_large_mod.kml")
data = docs.read()
xmldoc = mini.parseString(data)
import xml.etree.ElementTree as et
root = et.fromstring(data)

for ele in root.getiterator():
	if "Point" in ele.tag:

"""
import os
import re


def replacetags(i):
	a = ""
	b = i
	if "&gt;" in i and "&lt;" in i:
		a = i.replace("&gt;",">")
		b = a.replace("&lt;","<")
	return b

os.chdir("/Users/Winza/Documents/projects/MTapp")
import xml.etree.ElementTree as ET
tree = ET.parse("wms_train.kml")
rootit = tree.getroot().getiterator()
lst = []
lst2 = []
for i in rootit:
	if i.tag.endswith("Style"):
		lst.append(i)
	elif i.tag.endswith("LookAt"):
		lst2.append(i)

root = tree.getroot()
for parents in root[0][1]:
	print parents
	for i in lst:
		if i in parents:
			parents.remove(i)
	for j in lst2:
		if j in parents:
			parents.remove(j)

tree.write("modified_trains.kml")

file = open("modified_trains.kml","r")
lst2 = []
lst = file.readlines()
for i in lst:
	if re.match("^\s*$",i):
		pass
	else:
		newi = replacetags(i)
		lst2.append(newi)

file = open("newtrainlines.kml","w")
file.writelines(lst2)
file.close





