# Desafio 022 (Aula 09)
#
# Crei um programa que leia o nome completo de uma pessoa e mostre:
#
# . O nome com todas a letras maiúsculas
# . O nome com todas a letras minúsculas
# . Quantas letras ao todo (sem considerar espaços)
# . Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip()

print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome é {} e tem {} letras'.format(nome[0:nome.find(' ')], nome.find(' ')))

#dividido = nome.split()
# print(dividido)
# print(''.join(dividido))
# print(len(''.join(dividido)))
#print('Seu nome tem ao todo {} letras'.format(len(''.join(dividido))))
#print('Seu primeiro nome é {} e tem {} letras'.format(dividido[0], len(dividido[0])))
