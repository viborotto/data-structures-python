# sequence of values, qualquer tipo, elementos da lista
list1 = [1, 2, 3, 4, 5, 6]
list2 = ['banana', 'pera', 'maca', 'uva']
list3 = ['uva', 0.1, 3, 'hello']
list4 = ['vi', 21, [17.123]]
empty_list = []

# unlike strings, lists are mutable, can be change the value of an element
print(list1[0])
list1[0] = 0
print(list1)

# Operator IN

cheeses = ['Cheddar', 'Edam', 'Gouda']
'Edam' in cheeses
# element by element
for cheese in cheeses:
    print(cheese)

for i in range(len(list1)):
    list1[i] = list1[i] * 2

# Operations in Lists
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
c = a + b
print(c)

repeat = [0] * 4
print(repeat)

# Slice List
t = ['a', 'b', 'c', 'd', 'e', 'f']
print(t[1:3])
# update multiple elements
t = ['a', 'b', 'c', 'd', 'e', 'f']
t[1:3] = ['x', 'y']
print(t)

# Methods for Lists
t.append('d')  # add in final
t1 = ['a', 'b']
t2 = ['c', 'd']
t1.extend(t2)
print(t1)
t1.sort()  # sort list

# delete element
x = t.pop(1)
t = ['a', 'b', 'c']
del t[1]
y = ['a', 'b', 'c']
y.remove('b')
t = ['a', 'b', 'c', 'd', 'e', 'f']
del t[1:5]

t = ['a', 'b', 'c', 'd', 'e', 'f']
# Lists and Functions
len(t)
max(t)
min(t)
sum(a)
sum(a) / len(a)
# sum only when list of numbers

# calcular media dos numeros inseridos por um usuario
count = 0
while (True):
    inp = input('Enter a number: ')
    if inp == 'done': break
    value = float(inp)
    total = total + value
    count = count + 1
average = total / count
print('Average:', average)

# Lists and Strings
s = 'spam'
t = list(s)
print(t)

s = 'sentindo falta dos fiordes'
v = s.split()
print(v)

s = 'spam-spam-spam'
delimiter = '-'
s.split(delimiter)

# JOIN is the inverse of split
t = ['sentindo', 'falta', 'dos', 'fiordes']
delimiter = ' '
delimiter.join(t)

# Align lines
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    print(words[2])

# Object and Values
a = 'banana'
b = 'banana'
a is b

a = [1, 2, 3]
b = [1, 2, 3]
a is b


# this two lists are equivalent but not identic, only values are equals

# Aliados
# A associação de uma variável a um objeto é chamada de referência.
# Um objeto com mais de uma referência possui mais de um nome, então dizemos que o objeto é aliado.

# Lists with argument

# Quando você passa uma lista como argumento de uma função, a função recebe uma referência a essa lista

def remove_primeiro_elemento(t):
    del t[0]





fname = open(raw_input("Enter file name: "))

print ("ERROR: Invalid file name")
exit()
lst = list()

for line in fname:
    line = line.rstrip()
    l = line.split(" ")
for words in l:
    if words in lst:
        continue
    else:
    lst.append(words)
    lst.sort()
    print lst

