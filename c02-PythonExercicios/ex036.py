# Desafio 036 (Aula 12)
#
# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai
# perguntar o 'valor da casa', o 'salário' do comprador e em 'quantos anos' ele vai pagar.
#
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder '30%' do salário ou então o
# empréstimo será negado.
#

casa = float(input('Valor da casa: R$ '))
sal = float(input('Salário do comprador: R$ '))
anos = int(input('quantos anos de financiamento: '))

prest = casa / (anos * 12)
min = sal * 0.30

# print('Para pagar uma casa de R$ {:.2f} em {} anos a prestação será de R$ {:.2f}'.format(casa, anos, prest))
# print(min)
print('Para pagar uma casa de R$ {:.2f} em {} anos '.format(casa, anos), end='')
print('a prestação será de R$ {:.2f}'.format(prest))

if prest <= min:
    print('Empréstimo APROVADO!!!')
else:
    print('Empréstimo NEGADO!')

