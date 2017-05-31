#!/usr/bin/env python3
import sys, os
import zipfile
import xml.etree.ElementTree as ET

def main():
	zf = zipfile.ZipFile(sys.argv[1], 'r')
	print("files: " + str(zf.namelist()))
	print("roading rocket.ork ...")
	xml = ET.fromstring(zf.read("rocket.ork"))
	rocket = xml.find('rocket')
	print("rocket:")
	print("  name: "		+ rocket.find('name').text)
	print("  comment: "		+ rocket.find('comment').text)
	print("  designer: "	+ rocket.find('designer').text)
	
	stage = rocket.find('stage')
	
	

if __name__ == '__main__':
	main()
