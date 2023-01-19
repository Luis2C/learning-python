# Desafio 035 (Aula 10)
#
# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem
# ou não formar um triângulo.
#

print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)

seg1 = float(input('Primeiro segmento: '))
seg2 = float(input('Segundo segmento: '))
seg3 = float(input('Terceiro segmento: '))

if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print('Os segmentos acima PODEM FORMAR um triângulo. PARABÉNS!!!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')
