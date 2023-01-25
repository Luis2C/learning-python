# Desafio 039 (Aula 12)
#
# Faça um programa que leia o ano de nascimento de um jovem e informe,de acordo com sua idade:
#
# - Se ele 'ainda vai se alistar' ao serviço militar.
# - Se é a 'hora de se alistar'.
# - Se já 'passou da tempo' do alistamento.
#
# Seu programa também deverá mostrar o tempo que faltou ou que passou do prazo.
#
# Plus++
# Perguntar o 'sexo' e caso seja do sexo 'M' efetua o calculo e se for 'F' (Feminino) diz que não precisa fazer o
# alistamento militar obrigatório.

from datetime import date

ano = date.today().year

nasc = int(input('Ano de nascimento: '))
sexo = str(input('Qual o seu sexo (M / F): '))
idade = ano - nasc

print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, ano))

if sexo == 'M':
    if idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE!')
    elif idade < 18:
        saldo = 18 - idade
        print('Ainda faltam {} anos para o alistamento'.format(saldo))
        print('Seu alistamento será em {}'.format(ano + saldo))
    elif idade > 18:
        saldo = idade - 18
        print('Você já deveria ter se alistado ha {} anos.'.format(saldo))
        print('Seu alistamento foi em {}'.format(ano - saldo))
elif sexo == 'F':
    print('Você não precisa fazer o Alistamento Militar Obrigatório')
else:
    print('Opção inválida. Tente novamente.')