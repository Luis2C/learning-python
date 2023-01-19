# Desafio 028 (Aula 10)
#
# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qualfoi o número escolhido pelo computador.
#
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
#

from random import randint
from time import sleep

comp = randint(0, 5)  # computador seleciona um número inteiro entre 0 e 5
# print('Pensei no número {}'.format(comp))

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

jog = int(input('Em que número eu pensei? '))  # jogador tenta adivinhar

print('PROCESSANDO...')
sleep(3)

if jog == comp:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(comp, jog))
