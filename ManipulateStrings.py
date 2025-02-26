# String is a sequence of char
# negative index count by final
name = "Vittoria"
first_letter = name[0]
name_length = len(name)
last_letter_name = name[-1]
print("My name is Vittoria, nice to meet you!")
print("First Letter Name:", first_letter)
print("Last Letter Name:", last_letter_name)

# Letter by letter, start by init:
index = 0
while index < len(name):
    letter = name[index]
    print(letter)
    index += 1
# start by final
index = len(name) - 1
while index > -1:
    letter = name[index]
    print(letter)
    index -= 1

# You can slice one string in Python, include the first number and exclude the last one
s = 'Monty Python'
print(s[0:5])
print(s[6:12])
print(name[:])

# Strings are immutable, not chance the char of string
hello = 'Hello World'


# For with Strings
def counting(word='banana', count=0):
    for x in word:
        if x == 'a':
            count += 1
    print(count)


counting()

# the operator in
'a' in 'hello'
# comparation between string for alphabetic order
# < antes, > depois, letras maiusculas vem antes de minuscukas para o python
# methods: dir(hello)
# hello.find()


data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
start = atpos+1
sppos = data.find(' ', atpos)
host = data[atpos+1:sppos]
print(host)

# formatation operator, %d int, %g float, %s string
camel = 42
print('During %d years I saw %g %s.' % (3, 0.1, 'camelos'))

#Exercise1: extrac string after ':' and convert into float
y = 'X-DSPAM-Confidence:0.8475'
index_find = y.find(':')
index_value = y[index_find+1:]
print(float(index_value))

#Exercise2:Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
inp = fh.read()
count = 0
average = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    average += float(line[20:-1].strip())
    count += 1
print("Average spam confidence:",average/count)

