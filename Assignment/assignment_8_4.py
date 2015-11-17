fname = raw_input("Enter file name: ")
fh = open(fname)
string = fh.read().split()
#string is a list type
lst = list()
for line in string:
    try:
        line = lst.index(line)
        continue
    except:
        lst.append(line)
lst.sort()
print lst