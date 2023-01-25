# Desafio 037 (Aula 12)
#
# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a
# 'base de conversão':
#
# - 1 para 'binário'
# - 2 para 'octal'
# - 3 para 'hexadecimal'

num = int(input('Digite um número inteiro: '))

# print('Escolha uma das bases para conversão:')
# print('[ 1 ] converter para BINÁRIO')
# print('[ 2 ] converter para OCTAL')
# print('[ 3 ] converter para HEXADECIMAL')

print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')

base = int(input('Sua opção: '))

# if base == 1:
#     print('{} convertido para BINÁRIO = {}'.format(num, bin(num)))
# elif base == 2:
#     print('{} convertido para OCTAL = {}'.format(num, oct(num)))
# elif base == 3:
#     print('{} convertido para HEXADECIMAL = {}'.format(num, hex(num)))
# else:
#     print('Opção inválida. Tente novamente.')

# Fatiamento de string
if base == 1:
    print('{} convertido para BINÁRIO = {}'.format(num, bin(num)[2:]))
elif base == 2:
    print('{} convertido para OCTAL = {}'.format(num, oct(num)[2:]))
elif base == 3:
    print('{} convertido para HEXADECIMAL = {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente.')
