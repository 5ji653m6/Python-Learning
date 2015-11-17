name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
words = list()
counts = dict()
for line in handle:
    if not line.startswith('From '):
        continue
    words = line.rstrip().split()
    committer = words[1]
    counts[committer] = counts.get(committer,0) + 1

bigcount = None
bigword = None
for key,value in counts.items():
    if bigcount is None or value > bigcount:
        bigcount = value
        bigword = key
print bigword, bigcount
