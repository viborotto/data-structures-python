name = input("Enter file:")
fh = open(name)
counts = dict()
bigword = None
bigcount = None
if len(name) < 1:
    name = "mbox-short.txt"
##enontrar quem enviou
for line in fh:
    if line.startswith('From '):
        words = line.split() #transformei a linha em uma lista
        email = words[1]
        counts[email] = counts.get(email, 0) + 1
handle = open(name)
for word, count in counts.items() :
    if bigcount is None or count > bigcount :
        bigword = word
        bigcount = count
print(bigword,bigcount)
