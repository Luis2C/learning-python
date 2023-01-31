# Desafio 054 ( Aula 13 )
#
# Crie um programa que leia o 'ano de nascimento' de 'sete pessoas'. No final mostre quantas pessoas
# ainda não atingiram a maioridade e quantas já são maiores. ( considerar 21 sendo maoridade )

from datetime import date

atual = date.today().year

# Explo. 01 ( tentativa )
# nasc = int(input('Em que ano a 1º pessoa nasceu? '))
# idade = atual - nasc
#
# # print('Essa pessoa tem {} anos'.format(idade))
#
# if idade >= 21:
#     print('Essa pessoa é maior')
# else:
#     print('Essa pessoa é menor')

# Explo. 02 ( tentativa )
maior = 0
menor = 0

for pes in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(pes)))
    idade = atual - nasc

    if idade >= 21:
        maior += 1
    else:
        menor += 1

print('Ao todo tivemos {} pessoas maiores de idade'.format(maior))
print('E também tivemos {} pessoas menores de idade'.format(menor))
