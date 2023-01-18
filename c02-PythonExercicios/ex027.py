# Desafio 027 (Aula 09)
#
# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
#
# Ex:
# Digite o nome completo: Ana Maria de Souza
# primeiro = Ana
# último = Souza

nome = str(input('Digite seu nome completo: ')).strip()
divide = nome.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(divide[0]))
print('Seu último nome é {}'.format(divide[len(divide)-1]))
