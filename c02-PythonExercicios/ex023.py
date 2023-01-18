# Desafio 023 (Aula 09)
#
# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
#
# Ex:
# Digite um número: 1834
#
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1

num = int(input('Digite um número: '))
# Forma string - Para casos de número de 4 posições funciona, menor que isso não
# n = str(num)
#
# print('unidade: {}'.format(n[3]))
# print('dezena: {}'.format(n[2]))
# print('centena: {}'.format(n[1]))
# print('milhar: {}'.format(n[0]))

# Forma matemática
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('unidade: {}'.format(u))
print('dezena: {}'.format(d))
print('centena: {}'.format(c))
print('milhar: {}'.format(m))
