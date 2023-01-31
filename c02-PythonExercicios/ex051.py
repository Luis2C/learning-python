# Desafio 051 ( Aula 13 )
#
# Desenvolva um programa ue leia o 'primeiro termo' e a 'razão' de uma 'PA'. No final, mostre os '10'
# primeiros termos dessa progressão.

print('=' * 35)
print('{:^35}'.format(' 10 TERMOS DE UMA PA '))
print('=' * 35)

pri = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
dec = pri + (10 -1) * raz  # Obter o décimo termo de uma PA

for cont in range(pri, dec + raz, raz):
    print('{}'.format(cont), end=' -> ')

print('Acabou!')
