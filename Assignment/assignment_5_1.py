largest = None
smallest = None
while True:
    inp = raw_input("Enter a number: ")
    if inp == "done" : break
    
    try:
        num = int(inp)
    except:
        print "Invalid input"
        continue
    if num > largest:
        largest = num
    if num < largest:
        smallest = num

print "Maximum is", largest
print "Minimum is", smallest