# Desafio 008 ( Aula 07 )
#
# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

n = float(input('Digite um valor em metros: '))
c = n * 100
m = n * 1000

print('O valor de {} metros convertido em centímetros é {} e em milímetros é {}.'.format(n, c, m))
