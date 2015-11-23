import urllib
import xml.etree.ElementTree as ET

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'

#while True:
address = raw_input('Enter location: ')
#if len(address) < 1:break
uh = urllib.urlopen(address)
data = uh.read()
stuff = ET.fromstring(data)
lst = stuff.findall('comments/comment') # comments/comment is the path of XML content using expression, and output the result as a list format output as "lst"
# print lst,'\n\n'  --> for this line of code, we could get a list format. But the output are composed in the etree code from
# as lst is list format we could go through the lst to print out the name we find
count = 0
number_addup = 0
for item in lst:
#    print 'Name who possesses number: ', item.find('name').text
	number_addup = number_addup + int(item.find('count').text)
	count = count + 1
#    print 'Attribute', item.get("x"), '\n'
print 'Retrieving: ', address
print 'Retrieving ', len(data), 'characters'
print 'Count: ', count
print 'Sum: ', number_addup
