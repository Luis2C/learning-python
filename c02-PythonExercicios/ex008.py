# Desafio 008 ( Aula 07 )
#
# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
# km  hm  dam  m  dm  cm  mm -> Quilometros, Hectometros, Decametros, metros, decimetros, centimetros, milimetros

mt = float(input('Digite um valor em metros: '))
cm = mt * 100
mm = mt * 1000
dm = mt * 10
dam = mt / 10
hm = mt / 100
km = mt / 1000

print('A medida de {}m correponde a {:.0f}cm e {:.0f}mm'.format(mt, cm, mm))

# Plus ++
print('{}km'.format(km))
print('{}hm'.format(hm))
print('{}dam'.format(dam))
print('{}m'.format(mt))
print('{:.0f}dm'.format(dm))
print('{:.0f}cm'.format(cm))
print('{:.0f}mm'.format(mm))

