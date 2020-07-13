# Lib 're'
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line):
        print(line)

# Search for lines that start with 'From'
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line):
        print(line)
    if re.search('^F..m:', line):
        print(line)
# A string de pesquisa ˆFrom:.+@ irá combinar com sucesso linhas que comece com “From:”, seguido de um ou mais caracteres (.+), seguido por um sinal de arroba.


# Extractiong Data with RegularExpressions

x = 'My 2 favorites numbErs are 23 and 11'
y = re.findall('[0-9]+', x)
print(y)
y = re.findall('[AEIOU]+', x)
print(y)


# GREEDY MATCHING
# the repeat characters(* and +) push outward in both directions(greedy) to match the largest possible string
x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)

# NON-GREEDY MATCHING
x = 'From: Using the : character'
y = re.findall('^F.+?:', x)
print(y)

# Fine-Tuning String Extraction
x = 'From vittoria.borotto@uct.ac.za Sat Jan 5 09:22:14 2020'
y = re.findall('\S+@\S+', x)
print(y)

# Parentheses are not part of the match - but they tell where to START and STOP what string to extract
y = re.findall('^From (\S+@\S)', x)
print(y)

# The Double Split Pattern: Sometimes we split a line one way, and then grab one of the pieces of the line and split that piece again
words = x.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])
# But with Regular expressions the way is more easy:
lin = 'From vittoria.borotto@uct.ac.za Sat Jan 5 09:22:14 2020'
w = re.findall('@([^ ]*)', lin)
print(w)
# [^ ] = match non-blank character



hand = open('file.txt')
numList = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1:
        continue
    num = float(stuff[0])
    numList.append(num)
print('Maximum:', max(numList))

# Escape Character: if you want a special regular expression character to just behave normally(most of the time) you prefix with '\'
x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+', x)
print(y)
