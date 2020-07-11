# Open File, if doesnt exist, will fail, is a sequence lines
file = open('read.txt')
print(file)

# Read File
count = 0
for line in file:
    count = count + 1
print('Line Count:', count)
inp = file.read()
print(inp[:20])

# Searching through a file
for line in file:
    line = line.rstrip()
    if line.startswith('Vittoria'):
        print(line)
    if not line.startswith('Vittoria'):
        continue
    print(line)

# User choose the file name
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)

# 7.1 Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. Use the file words.txt to produce the output below.
fname = input("Enter file name: ")
fh = open(fname)
inp = fh.read()
print(inp.upper().strip())
