# Desafio 025 (Aula 09)
#
# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
#

nome = str(input('Digite o nome completo da pessoa: ')).strip()
print('Seu nome tem "SILVA"? {}'.format('SILVA' in nome.upper()))
