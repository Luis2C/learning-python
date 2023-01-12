n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
dr = n1 % n2
e = n1 ** n2
print('\n[{:^30}]'.format('Com Quebra de Linha'))
print('A soma é {}, o produto é {} e a divisão é {}'.format(s, m, d))
print('A divisão inteira é {}, \no resto da divisão é {} \ne a potência é {}'.format(di, dr, e))

print('\n[{:^30}]'.format('Sem Quebra de Linha'))
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d), end=' - ')
print('A divisão inteira é {}, o resto da divisão é {} e a potência é {}'.format(di, dr, e))
