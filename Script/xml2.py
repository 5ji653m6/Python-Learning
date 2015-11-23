import xml.etree.ElementTree as ET

input = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
	<user x="agent">
	    <id>007</id>
	    <name>James Bond</name>
	</user>
    </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user') #users/user is the path of XML content, and output the result as a list format output as "lst"
print 'User count:', len(lst) #count how many users are there within the <stuff> block
# print lst,'\n\n'  --> for this line of code, we could get a list format. But the output are composed in the etree code from

# as lst is list format we could go through the lst to print out the name we find
for item in lst:
    print 'Name', item.find('name').text
    print 'Id', item.find('id').text
    print 'Attribute', item.get("x"), '\n'

