# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup
import os

#siteUrl = "http://guildedage.net/comic/chapter-1-cover/" #first page
siteUrl = "http://guildedage.net/comic/chapter-1-cover/"
lastUrl = " "
comicUrl = " "
comicName = "guildedAge_"
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
	for link in soup.find_all(rel="next"):
		siteUrl = link.get("href")
	links = soup.find_all('div',id="comic")
	for l in links:
		for l2 in l.find_all('img'):
			comicUrl = l2.get("src")
			if comicUrl is not None:
				f = open(comicName + str (fileNumber) + '.jpg','wb')
				f.write(urllib2.urlopen(comicUrl).read())
				f.close()
				fileNumber += 1
	if siteUrl == lastUrl:
		break

print ("Download Complete")
