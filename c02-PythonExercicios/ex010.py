# Desafio 010 ( Aula 07 )
#
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dolares ela pode comprar.
#
# Considere: US$ 1,00 = R$ 3,27

real = float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = real / 3.27

# Plus ++ ( fazer para )
# euro
# ien

print('Com R$ {:.2f} você pode comprar US$ {:.2f}!'.format(real, dolar))
