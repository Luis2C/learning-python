# Desafio 017 (Aula 08)
#
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
#

# Explo 01
# co = float(input('Comprimento do cateto oposto: '))
# ca = float(input('Comprimento do cateto adjacente: '))
#
# hi = (co ** 2 + ca ** 2) ** (1/2)
#
# print('A hipotenusa vai medir {:.2f}'.format(hi))
# 2 2.5 -> 3.20

# Explo 02
#import math
from math import hypot

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

#hi = math.hypot(co, ca)
hi = hypot(co, ca)

print('A hipotenusa vai medir {:.2f}'.format(hi))
# 2 2.5 -> 3.20
