# Cores no Terminal

# Style                Text      ( cor )    Background
# 0 - None              30  -->   Branco     <--  40
# 1 - Bold              31  -->   Vermelho   <--  41
# 4 - Undeline          32  -->   Verde      <--  42
# 7 - Negative          33  -->   Amarelo    <--  43
#     (inverte)         34  -->   Aul        <--  44
#                       35  -->   Lilas      <--  45
#                       36  -->   Magenta    <--  46
#                       37  -->   Cinza      <--  47
#
# Obs.: Pesquisar 'Colorize'
#
# \033[0;30;41m
# \033[4;33;44m
# \033[1;35;43m
# \033[30;42m
# \033[m (desfaz todas as configurações)
# \033[7;30m

# print('Olá Mundo!')
# print('\033[31mOlá Mundo!')
# print('\033[31;43mOlá Mundo!')
# print('\033[1;31;34mOlá Mundo!')
# print('\033[1;31;34mOlá Mundo!\033[m')
# print('\033[4;30;45mOlá Mundo!\033[m')
# print('\033[7;30;45mOlá Mundo!\033[m')
# print('\033[0;33;44mOlá Mundo!\033[m')
# print('\033[7;33;44mOlá Mundo!\033[m')

# Explo. 01
# a = 3
# b = 5
#
# print('Os valores são {} e {}'.format(a, b))
# print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))


# Explo. 02
# nome = 'Clark Kent'
#
# print('Olá! Prazer em te conhecer, {}!!!'.format(nome))
# print('Olá! Prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))


# Explo. 03
nome = 'Clark Kent'
cores = {'limpa': '\033[m', 'azul': '\033[34m', 'amarelo': '\033[33m', 'pretoebranco': '\033[7;40m'}

print('Olá! Prazer em te conhecer, {}!!!'.format(nome))
print('Olá! Prazer em te conhecer, {}{}{}!!!'.format(cores['amarelo'], nome, cores['limpa']))
print('Olá! Prazer em te conhecer, {}{}{}!!!'.format(cores['pretoebranco'], nome, cores['limpa']))

