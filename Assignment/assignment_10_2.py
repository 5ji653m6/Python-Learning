name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
string = list()
counts = dict()
for line in handle:
    if not line.startswith('From '):
        continue
    string = line.split()
    time = string[5].split(':')
    hour = time[0]
    counts[hour] = counts.get(hour,0) + 1
tuple_time = counts.items()
tuple_time.sort()
for hr, count in tuple_time:
    print hr, count