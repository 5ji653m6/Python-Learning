import urllib
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address}) # the urllib.urlencode extract the input from address and combind with the url we are looking for.
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'

    try: js = json.loads(str(data)) # if the json format is bad, then the json.loads might blow up.
    except: js = None
    if 'status' not in js or js['status'] != 'OK': # if boolean test is to check if whether js is None, or the js haven't a status "OK" in the content. If so, then print out a string, then prompt for input again.
        print '==== Failure To Retrieve ===='
        print data
        continue

    print json.dumps(js, indent=4) # the parsed json is in dictionary format, then we do the "pretty printing"

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print 'lat',lat,'lng',lng
    location = js['results'][0]['formatted_address']
    print location


