# Desafio 048 ( Aula 13 )
#
# Faça um programa que calcule a 'soma' entre todos os 'números ímpares' que são 'multiplos de três' e
# que se encontram no intervalo de '1' até '500'.

# Explo. 01
# soma = 0
# qtd = 0
# for cont in range(1, 501):
#     if cont % 2 != 0 and cont % 3 == 0:
#         qtd += 1
#         soma += cont
#
# print('A soma de todos os {} valores solicitados é {}'.format(qtd, soma))

# Explo. 02
soma = 0
qtd = 0

for cont in range(1, 501, 2):
    if cont % 3 == 0:
        qtd += 1
        soma += cont

print('A soma de todos os {} valores solicitados é {}'.format(qtd, soma))
