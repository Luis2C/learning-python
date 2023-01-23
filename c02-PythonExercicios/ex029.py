
# Desafio 029 (Aula 10)
#
# Escreva um programa que leia a velocidade de um carro.
#
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#
# A multa vai custar R$7,00 por cada Km acima do limite.
#

veloc = float(input('\033[36mQual a velocidade atual do carro? '))

if veloc > 80:
    print('\033[1;31mMULTADO! Você excedeu o limite permitido que é de 80Km/h')
    multa = (veloc - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))

print('\033[1;34mTenha um bom dia! Dirija com segurança!')
