"""
author : rishabh 
"""
import csv
import MySQLdb
import urllib2
import re
from time import sleep

maxid = 10000
minid = 3
ids = 1
b_state = 0

while ids < maxid:
	url = "http://facebook.com/profile.php?id="+str(ids)
	try:
		u = urllib2.urlopen(url)
	
		e = re.compile('<title*[^>]*>.*</title*>')
		data = u.read()

		current =  e.findall(data)

		if "Unavailable" in current[0] or "Not Found" in current[0]:
			b_state = 1
		else:
		 	
		 	match = re.search(r'URL=/?([^?>]+)',data)
		 	#if ("/" in match):
		 	#	match = re.search(r'people/?([^/>]+)',data)

		 	
			newemail =  str(match.group(1))+"@Facebook.com"	
			print newemail
			with open("facebookname.txt", "a") as myfile:
				myfile.write(newemail + "\n")
	except:
		b_state = 1	
	ids+=1
