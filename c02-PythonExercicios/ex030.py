# Desafio 030 (Aula 10)
#
# Crie um programa que leia um número inteiro qualquer e mostre na tela se ele é PAR ou Ímpar.
#

num = int(input('\033[1;35mDigite um número qualquer? '))

resto = num % 2

# if resto == 0:
#     print('O número {} é PAR!'.format(num))
# else:
#     print('O número {} é ÍMPAR!'.format(num))

print('\033[33mO número \033[1;40m{}\033[m é \033[7;30;43m{}\033[m!'.format(num, 'PAR' if resto == 0 else 'ÍMPAR'))
