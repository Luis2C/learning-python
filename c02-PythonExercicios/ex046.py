# Desafio 046 ( Aula 13 )
#
# Faça um programa que mostre na tela um 'contagem regressiva' pra o estouro de fogos de artifício, indo
# de '10 até 0', com uma pausa de '1 segundo' entre eles. ( 'BUM!!!' adicionar 'emoji' )

from time import sleep
import emoji

print('Contagem Regressiva')
for i in range(10, -1, -1):
    print(i)
    sleep(1)

print(emoji.emojize(":bomb: :bomb: BUM! BUM! POOOW! :bomb: :bomb:", language='alias'))
