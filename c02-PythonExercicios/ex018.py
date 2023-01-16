# Desafio 018 (Aula 08)
#
# Faça um programa que leia o ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
#

#import math
from math import radians, sin, cos, tan

an = float(input('Digite o ângulo que você deseja: '))

#rd = math.radians(an)  # converte o ângulo em radianos e acha o seno dele
#se = math.sin(rd)
#co = math.cos(rd)
#tg = math.tan(rd)

rd = radians(an)  # converte o ângulo em radianos para usar no seno, cosseno e tangente
se = sin(rd)
co = cos(rd)
tg = tan(rd)

print('O ângulo de {} tem o SENO de {:.2f}'.format(an, se))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(an, co))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(an, tg))
#30 -> 0.50 0.87 0.58
#45 -> 0.71 0.71 1.00
