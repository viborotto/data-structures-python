# Is like a list, the index can be anytype
# key-value, the key map the value
# function DICT create a dictionary
ing2port = dict()
print(ing2port)  # empty dictionary {}

ing2port['one'] = 'um'
print(ing2port)
ing2port = {'one': 'um', 'two': 'dois', 'three': 'três'}
# dont has order

print(ing2port['two'])
# Can be use len() and IN like in Lists and Strings

vals = list(ing2port.values())
'um' in vals

# Dictionary like a count group
# Você pode criar um dicionário, estabelecendo caracteres como chaves e conta- dores como os valores correspondentes. A primeira vez em que um caractere for lido, um novo item seria adicionado ao dicionário. Após isso, o valor de um item existente seria incrementado.
palavra = 'brontosaurus'
d = dict()
for c in palavra:
    if c not in d:
        d[c] = 1
    else:
        d[c] = d[c] + 1
print(d)

# Method get(key,value)
word = 'brontosaurus'
d = dict()
for c in palavra:
    d[c] = d.get(c, 0) + 1
print(d)

# Dictionary and File
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
print(counts)

# Loops and Dictionaries

conta = {'chuck': 1, 'annie': 42, 'jan': 100}
for chave in conta:
    print(chave, conta[chave])

a = {'chuck': 1, 'annie': 42, 'jan': 100}
lst = list(counts.keys()) # listas de chaves
print(lst)
lst.sort()
for key in lst:
    print(key, counts[key])



# What is the purpose of the second parameter of the get() method for Python dictionaries?
# To provide a default value if the key is not found