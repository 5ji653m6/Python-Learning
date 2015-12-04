import urllib
import json


#while True:
address = raw_input('Enter location: ')
print "Retrieving: ", address
#if len(address) < 1:break
uh = urllib.urlopen(address)
data = uh.read()
#print data
info = json.loads(str(data))
jsonStr = json.dumps(info, indent = 4)
#print info
#print type(info)

#print jsonStr
#print type(jsonStr)

counter = 0
sumup = 0
while True:
 try:
  print 'Name', info["comments"][int(counter)]["name"]
 except: break
 print 'Count', info["comments"][int(counter)]["count"]
 count = info["comments"][int(counter)]["count"]
 counter = counter + 1
 sumup = sumup + count

print "\n\nCount: ", counter
print "The sumup is: ", sumup
