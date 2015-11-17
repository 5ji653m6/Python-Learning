# Use words.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
upcs = fh.read()
upcs_nonewline = upcs.rstrip().upper()
print upcs_nonewline
