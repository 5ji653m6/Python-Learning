import urllib
from BeautifulSoup import *
url = raw_input('Enter - ')

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

#Retrieve a list of the anchor tags
#Each tag is like a dictionary of HTML attributes

tags = soup('span')
summy = 0
for tag in tags:
	#Look at the parts of a tag
	print 'TAG: ', tag
	print 'URL: ', tag.get('href', None)
	print 'Content: ', tag.contents[0]
	print 'Attrs: ', tag.attrs
	summy = summy + int(tag.contents[0])
print 'The Sum-up of this file is: \n', summy
