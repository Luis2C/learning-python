# Desafio 020 (Aula 08)
#
# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
#

#import random
from random import shuffle

a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')

lista = [a1, a2, a3, a4]
#random.shuffle(lista)
shuffle(lista)

print('A ordem de apresentação será')
print(lista)
