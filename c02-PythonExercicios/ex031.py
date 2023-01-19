# Desafio 031 (Aula 10)
#
# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
#

dis = float(input('Qual é a distância da sua viagem? '))

print('Você está prestes a começar uma viagem de {:.1f}Km.'.format(dis))

# if dis <= 200:
#     val = dis * 0.50
# else:
#     val = dis * 0.45

val = dis * 0.50 if dis <= 200 else dis * 0.45

print('E o preço da sua passagem será de R${:.2f}'.format(val))
