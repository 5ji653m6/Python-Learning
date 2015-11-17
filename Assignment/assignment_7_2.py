# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
flt_sum = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    flt_start = int(line.find('0'))
    flt_sum = flt_sum + float(line[flt_start:])
    count = count + 1
print "Average spam confidence:", flt_sum/count