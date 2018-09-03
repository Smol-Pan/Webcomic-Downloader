# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup
import os

#siteUrl = "http://www.girlgeniusonline.com/comic.php?date=20021104" #first page
siteUrl = "http://www.girlgeniusonline.com/comic.php?date=20021104"
lastUrl = " "
comicUrl = " "
comicName = "girlGenius_"
fileNumber = 1

print( "Testing for directory " + comicName + " in current directory")
if os.path.isdir(os.getcwd() + comicName) == True:
	print( "Directory " + comicName + " exists")
else:
	print( "Directory " + comicName + " does not exist")
	os.mkdir(comicName)
	print( "Directory " + comicName + " created")
os.chdir(os.getcwd() + comicName)
print( "Moved to " + comicName)

while True:
	lastUrl = siteUrl
	page = urllib2.urlopen(siteUrl)
	soup = BeautifulSoup(page, "html.parser")
	for link in soup.find_all(title="The Next Comic"):
		siteUrl = link.get("href")
	for link in soup.find_all('img',alt='Comic'):
		comicUrl = link.get("src")
		if comicUrl is not None:
			f = open(comicName + str (fileNumber) + '.jpg','wb')
			f.write(urllib2.urlopen(comicUrl).read())
			f.close()
		else
			print (lastUrl + "Failed to download")
		fileNumber += 1
	if siteUrl == lastUrl:
		break

print ("Download Complete")
