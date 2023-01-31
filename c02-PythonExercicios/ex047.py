# Desafio 047 ( Aula 13 )
#
# Crie um programa que mostre na tela 'todos os números pares' que estão no intervalo entre '1' e '50'.

# Explo. 01
# for cont in range(1, 51):
#     if cont % 2 == 0:
#         print('{} '.format(cont), end='')
#
# print('Acabou!')

# Explo. 02
for cont in range(2, 51, 2):
    print('{} '.format(cont), end='')

print('Acabou!')
