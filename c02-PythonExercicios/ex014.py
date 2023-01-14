# Desafio 014 ( Aula 07 )
#
# Escreva um programa que apartir de uma temperatura digitada em °C a converta para °F.

c = float(input('Informe a temperetura em °C: '))
f = ((9 * c) / 5) + 32
#f = 9 * c / 5 + 32    # a ordem de procedencia não afeta o resultado sem o parenteses. (para esta formula)
print('A temperatura de {:.1f}°C corresponde a {}°F!'.format(c, f))
