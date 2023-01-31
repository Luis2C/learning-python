# 13 - Estruturas de Controle: Estrutura de Repetição 'for' ( Laços de Repetições ou Iterações )
# [ Parte 1 ]

# print('Oi')
# print('Oi')
# print('Oi')
# print('Oi')
# print('Oi')
# print('Oi')

# Obs.: No 'for' nâo considera o ultimo número (vai contar até o anterior no caso '5') e sai do laço. Para iterar 6
#       vezes informamos de '(0, 6)' e não '(1, 6).

# Explo.01
# for c in range(1, 6):
# for c in range(0, 6):
#     print('Oi')
#
# print('Fim')

# Explo.02
# for c in range(0, 6):
#     print(c)
#
# print('Fim')

# Explo.03
# Não faz o laço
# for c in range(6, 0):
#     print(c)
#
# print('Fim')

# Faz o laço na ordem decrescente
# for c in range(6, 0, -1):
#     print(c)
#
# print('Fim')

# Laço com salto
# for c in range(0, 7, 2):
#     print(c)
#
# print('Fim')

# Explo.04
# n = int(input('Digite um número: '))
#
# for c in range(0, n+1):
#     print(c)
# print('Fim')

# Explo.05
# i = int(input('Início: '))
# f = int(input('Fim: '))
# p = int(input('Passo: '))
#
# for c in range(i, f+1, p):
#     print(c)
# print('Fim')

# Explo.06
s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n  # mesma coisa que 's = s + n'

print('A somatória de todos os valores foi {}'.format(s))
