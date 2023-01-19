# Estruturas Condicionais
# . Condições Simples
# . Condições Compostas
#

# Explo. 01
# nome = str(input('Qual o seu nome? '))
#
# if nome == 'Luis':
#     print('Que nome lindo você tem!')
# else:
#     print('Seu nome é tão normal!')
# print('Bom dia, {}'.format(nome))

# Explo. 02
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

m = (n1 + n2) / 2

print('A sua média foi {:.1f}'.format(m))
#print('PARABÉNS!' if m >= 6.0 else'ESTUDE MAIS!')

if m >= 6.0:
    print('Sua média foi boa! PARABÉNS!!!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!!!')
