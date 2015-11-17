# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

# Prompt for the friend list
url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
# Enter the link 7 times
enter_page = 0
while enter_page < 7:
	tags = soup('a')
	count = 0
	enter_page = enter_page + 1
	for tag in tags:
		count = count + 1
		print tag.get('href', None), count
		while count == 18:
			next = tag.get('href', None)
			break
	print 'Now is the page of: \n', enter_page
	print 'The 18th friend name is: \n', next
	print 'The last name is: \n', tag.get('href', None),'\n'
	url = next
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)