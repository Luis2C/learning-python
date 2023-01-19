# Desafio 030 (Aula 10)
#
# Crie um programa que leia um número inteiro qualquer e mostre na tela se ele é PAR ou Ímpar.
#

num = int(input('Digite um número qualquer? '))

resto = num % 2

# if resto == 0:
#     print('O número {} é PAR!'.format(num))
# else:
#     print('O número {} é ÍMPAR!'.format(num))

print('O número {} é {}!'.format(num, 'PAR' if resto == 0 else 'ÍMPAR'))
