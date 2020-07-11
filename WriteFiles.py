# For write a file, first, open with mode 'w'
fout = open('read.txt', 'w')
print(fout)
# se o arquivo ja existir nesse modo vai limpar, cuidado
line1 = "This is a new line content"
fout.write(line1)# retorna o numero de caracteres gravasdos
line2 = 'the emblem of our land.\n'
fout.write(line2)
fout.close()


# function repr, pega qualqier parametro como arrgumento e retorna uma representacao de sting, ate mesmo o \n

