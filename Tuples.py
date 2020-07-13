# Tuples like Strings are immutable, but anytype
t = ('a', 'b', 'c', 'd', 'e')
t1 = ('a',) # one element
type(t1)
# or we can create with a function
t = tuple()
t = tuple('lupins')
print(t)
print(t[1:3])

# Compare Tuples
(0, 1, 2) < (0, 3, 4)

txt = 'but soft what light in yonder window breaks' words = txt.split()
t = list()
for word in words:
    t.append((len(word), word))
    print(t)
t.sort(reverse=True)
res = list()
for length, word in t:
    res.append(word)
print(res)


# Atribuição de Tupla
m = [ 'se', 'divirta' ]
x, y = m
print(x)
print(y)
# Permutar valores das variaveis
x, y = y, x
# tupla de variaveis = tupla de expressoes
email = 'florzinha@hotmail.com'
nomedeusuario, dominiodoemail = email.split('@')


# Dictionaries and Tuples
d = {'a':10, 'b':1, 'c':22}
t = list(d.items())
print(t)
t.sort()

# Multipla atribuicao com Dicionarios
# percorrer a chave e valor de um dicionario em um unico item
for chave, valor in list(d.items()):
    print(valor, chave)

