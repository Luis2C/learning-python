# Desafio 044 (Aula 12)
#
# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu 'preço normal'
# e 'condição de pagamento':
#
# - à vista 'dinheiro/cheque': '10%' de desconto
# - à vista no 'cartão': '5%' de desconto
# - em até '2x no cartão': preço normal
# - '3x ou mais' no cartão: '20%' de juros

print('{:=^40}'.format(' LOJAS VENDE MAIS '))

preco = float(input('Preço das compras: R$ '))

print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')

opcao = int(input('Qual é a opção? '))

if opcao == 1:
    total = preco - (preco * 0.10)
elif opcao == 2:
    total = preco - (preco * 0.05)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R$ {:.2f} SEM JUROS'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 0.20)
    qtd = int(input('Quantidade de parcelas: '))
    parcela = total / qtd
    print('Sua compra será parcelada em {}x de R$ {:.2f} COM JUROS'.format(qtd, parcela))
else:
    total = preco
    print('\033[1;31mOpção INVÁLIDA de pagamento, tente novamente!\033[m')

print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(preco, total))
