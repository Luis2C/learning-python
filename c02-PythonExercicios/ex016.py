# Desafio 016 (Aula 08)
#
# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
#
# Ex:
# Digite um número: 6.127
# O número 6.127 tem a parte Inteira 6.

# import math
# from math import trunc

num = float(input('Digite um número: '))

# print('O número {} tem a parte Inteira {}.'.format(num, math.trunc(num)))
# print('O número {} tem a parte Inteira {}.'.format(num, trunc(num)))

# Sem 'import'
print('O número {} tem a parte Inteira {}.'.format(num, int(num)))
