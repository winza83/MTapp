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

def modifications():
	f = open("train_1.kml", "r")
	lst = []
	lst.append("<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\" ?> \n")

	for i in f.readlines():
		if ":ns0" in i or "ns0:" in i:
			j = i.replace(":ns0","")
			k = j.replace("ns0:","")
			lst.append(k)

	f2 = open("train1a.kml","w")
	f2.writelines(lst)
	f2.close()


os.chdir("/Users/Winza/Documents/projects/MTapp")

import xml.etree.ElementTree as ET
treeo = ET.parse("wms_train.kml")
tree2 = ET.parse("wms_train.kml")

rooto = treeo.getroot()
root2 = tree2.getroot()
root2[0][1].clear()

root2[0][1].extend((rooto[0][1])[0:100])
tree2.write("train_1.kml")

modifications()
