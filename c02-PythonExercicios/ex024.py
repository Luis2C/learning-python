# Desafio 024 (Aula 09)
#
# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
#

cidade = str(input('Digite o nome de uma cidade: ')).strip()
# divide = cidade.split()
# print('Começa com nome 'SANTO': {}'.format('SANTO' in divide[0].upper()))
#print('Começa com nome 'SANTO': {}'.format('SANTO' in cidade.upper().split()[0]))
print(cidade[:5].upper() == 'SANTO')
