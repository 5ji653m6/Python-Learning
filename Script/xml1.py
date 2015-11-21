# xml.etree.ElementTree is the library dealing with contract between python and XML
# https://docs.python.org/2/library/xml.etree.elementtree.html
import xml.etree.ElementTree as ET

#The ''' triple quote is the start of the XML paragraph, and it also ends with '''
data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
     +1 734 303 4456
   </phone>
   <email hide="yes"/>
</person>'''

#ET.fromstring is the deserialization for parsing the XML paragragh into what we are looing for
tree = ET.fromstring(data)
print 'Name:',tree.find('name').text
print 'Attr:',tree.find('email').get('hide')
