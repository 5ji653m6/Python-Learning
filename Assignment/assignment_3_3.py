# The score range from 0 exlusive to 1.0 inclusive

inpsc = raw_input('Enter Score:')

if float(inpsc) >= 0.9 and float(inpsc) <1:
    print "A"
if float(inpsc) >= 0.8 and float(inpsc) <0.9:
    print "B"
if float(inpsc) >= 0.7 and float(inpsc) <0.8:
    print "C"
if float(inpsc) >= 0.6 and float(inpsc) <0.7:
    print "D"
if float(inpsc) >0 and float(inpsc) <0.6:
    print "F"
    
elif float(inpsc) < 0:
    print "Score input must above 0 error!"
elif float(inpsc) > 1:
    print "Score input must below 1 error!"
    