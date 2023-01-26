# Desafio 042 (Aula 12)
#
# Refaça o 'DESAFIO 35' dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#
# - 'Equilátero': todos os lados iguis
# - 'Isósceles': dois lados iguias
# - 'Escaleno': Todos os lados diferentes

print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)

seg1 = float(input('Primeiro segmento: '))
seg2 = float(input('Segundo segmento: '))
seg3 = float(input('Terceiro segmento: '))

if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print('Os segmentos acima PODEM FORMAR um triângulo. ', end='')

    # if seg1 == seg2 and seg2 == seg3:
    if seg1 == seg2 == seg3:
        print('EQUILÁTERO!')
    # elif seg1 != seg2 != seg3:   # Na diferença devemos comparar todos os elementos entre eles.
    elif seg1 != seg2 != seg3 != seg1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')
