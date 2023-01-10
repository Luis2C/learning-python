# Desafio 00
#
# Crie um script Python que leia o dia, o mês e o ano de nascimento
# de uma pessoa e mostre uma mensagem com data formatada.
#
#  in: Dia =
#      Mês =
#      Ano =
# out: Você nasceu no dia 17 de Mar de 1978. Correto?


dia = input('Dia = ')
mes = input('Mês = ')
ano = input('Ano = ')

print('='*25)
#print('Você nasceu no dia ', dia, ' de ', mes, ' de ', ano, '. Correto?')
print('Você nasceu no dia {} de {} de {}. Correto?'.format(dia, mes, ano))
