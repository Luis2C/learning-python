# Desafio 050 ( Aula 13 )
#
# Desenvolva um programa que leia 'seis números inteiros' e mostre a soma apenas daqueles que forem 'pares'.
# Se o valor digitado for 'ímpar', desconsidere-o.

soma = 0
qtd = 0

for c in range(1, 7):
    n = int(input('Digite um número inteiro: '))

    if n % 2 == 0:
        soma += n
        qtd += 1

print('Você informou {} números pares e a soma foi {}'.format(qtd, soma))
