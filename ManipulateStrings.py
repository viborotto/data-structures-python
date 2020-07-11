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

# formatation operator