# Desafio 052 ( Aula 13 )
#
# Faça um programa que leia um 'número inteiro' e diga se ele é ou não um 'número primo'.

num = int(input('Digite um número (inteiro): '))
tot = 0

for cont in range(1, num + 1):
    if num % cont == 0:
        print('\033[1:33m', end='')
        tot += 1
    else:
        print('\033[1:31m', end='')

    print('{} '.format(cont), end='')

print('\n\033[mO número {} foi divisível {} vezes'.format(num, tot))

if tot == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
