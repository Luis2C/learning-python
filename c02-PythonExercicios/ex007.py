# Desafio 007 ( Aula 07 )
#
# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1 = int(input('Digite a primeira nota do aluno: '))
n2 = int(input('Digite a sgunda nota do aluno: '))
m = (n1 + n2) / 2

print('A média do aluno é: {:.1f}!'.format(m))
