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

print('\033[1;34m-=-' * 20)
print('\033[33mVou pensar em um número entre 0 e 5. Tente adivinhar...')
print('\033[1;34m-=-' * 20)

jog = int(input('\033[33mEm que número eu pensei? '))  # jogador tenta adivinhar

print('\033[35mPROCESSANDO...\033[m')
sleep(3)

if jog == comp:
    print('\033[1;32mPARABÉNS! Você conseguiu me vencer!')
else:
    print('\033[31mGANHEI! Eu pensei no número {} e não no {}!'.format(comp, jog))
