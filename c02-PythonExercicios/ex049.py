# Desafio 049 ( Aula 13 )
#
# Refaça o 'Desafio 009', mostrando a 'tabuada' de um número que o usuário escolher, só que agora
# utilizando um 'laço for'.

n = int(input('Digite um número para ver a tabuada: '))

print('-'*15)

for cont in range(1, 11):
    print('{} x {:2} = {:2}'.format(n, cont, n*cont))

print('-'*15)
