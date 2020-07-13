# O esquema básico desse problema é ler o arquivo,
# procurar números inteiros usando o re.findall (),
# procurando uma expressão regular de '[0-9] +' e depois
# convertendo as seqüências de caracteres extraídas em números inteiros
# e resumindo os números inteiros.

import re
data = open('regex_sum_728730.txt')
list1 = list()
for line in data:
    y = re.findall('[0-9]+', line)
    list1 = list1 + y
sum1 = 0
for x in list1:
    sum1 += int(x)
print(sum1)

# Python 3:
# import re
# print( sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] ) )
