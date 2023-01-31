# Desafio 053 ( Aula 13 )
#
# Crie um progrma que leia uma 'frase' qualquer e diga se ela é 'palíndromo', desconsiderando os espaços.
#
# Ex:
# APOS A SOPA,
# A SACADA DA CASA,
# A TORRE DA DERROTA,
# O LOBO AMA O BOLO,
# ANOTARAM A DATA DA MARATONA

frase = str(input('Digite uma frase: ')).strip().upper()  # 'strip' tira os espaços em branco do inicio e do final
palavras = frase.split()  # 'split' separou as palavras da frase
# print(frase)
junto = ''.join(palavras)  # concatena as palavras sem os espaços em branco
# print(junto)

# Explo. 01
# inverso = ''
#
# for letra in range(len(junto) - 1, -1, -1):
#     inverso += junto[letra]

# Explo. 02
inverso = junto[::-1]  # apenas esta linha substitui o 'Explo. 01' acima

print('O inverso de {} é {}'.format(junto, inverso))

if junto == inverso:
    print('A frase digitada é um Palíndromo')
else:
    print('A frase digitada não é um Palíndromo')

