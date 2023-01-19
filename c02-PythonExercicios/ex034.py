# Desafio 034 (Aula 10)
#
# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#
# Para salários superiores a R$1.250,00, calcule um aumento de 10%.
# Para salários inferiores ou iguais, o aumento é de 15%.
#

sal = float(input('Qual é o salário do funcionário? R$ '))

if sal <= 1250:
    novo = sal + (sal * 0.15)
else:
    novo = sal + (sal * 0.10)

print('Quem ganhava R$ {:.2f} passa a ganhar R$ {:.2f} agora'.format(sal, novo))
