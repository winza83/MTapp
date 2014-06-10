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

root = tree.getroot()

pmark = (root[0][1])
for i in pmark.getiterator():
	if i.tag.endswith('name'):
		lst.append(i.text)

lst2 = [(i.split("."))[-1] for i in lst]

lst3 = [int(i) for i in lst2 if i.isdigit() == True]
lst3.sort
lst4 = []
for i in lst3:
	if i not in lst4:
		lst4.append(i)

datacnt = (max(lst3) - min(lst3))  / 10
count = 0


#tree.write("test1.kml")
lst = root[0][1]._children
lst2 = []


for placemark in root[0][1]:
	if placemark not in lst and placemark not in lst2:
		((tree.getroot())[0][1]).remove(placemark)

