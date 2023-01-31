# Desafio 055 ( Aula 13 )
#
# Faça um programa que leia o 'peso' de 'cinco pessoas'. No final, mostre qual foi o 'maior' e o menor'
# peso lidos.

maior = 0
menor = 0

for pes in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(pes)))

    if pes == 1:  # na primeira vez o 'maior' e o 'menor' seram iguais
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('O maior peso lido foi de {:.1f} Kg'.format(maior))
print('O menor peso lido foi de {:.1f} Kg'.format(menor))
