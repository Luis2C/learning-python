# Desafio 010 ( Aula 07 )
#
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dolares ela pode comprar.
#
# Considere: US$ 1,00 = R$ 3,27

v = float(input('Quantidade de dinheiro da carteira (R$): '))
d = v / 3.27

print('Consegue comprar US$ {:.2f}!'.format(d))
