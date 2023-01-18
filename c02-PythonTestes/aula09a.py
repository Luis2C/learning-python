# 09 - Manipulando Textos
# . Fatiamento - o ultimo valor é sempre ignorado pelo 'python' no método de fatiamento.
# . Análise
# . Transformação
# . Divisão
# . Junção

frase = 'Curso em Vídeo Python'

print(frase)


# . Fatiamento - o ultimo valor é sempre ignorado pelo 'python' no método de fatiamento.
print(frase[3])
print(frase[3:13])  # vai até o indice 12 (omite o ultimo)
print(frase[:13])
print(frase[13:])
print(frase[1:15])
print(frase[1:15:2])
print(frase[1::2])
print(frase[::2])

print('Oi')

print('''Lorem Ipsum é simplesmente uma simulação de texto da indústria tipográfica e de impressos, 
e vem sendo utilizado desde o século XVI, quando um impressor desconhecido pegou uma bandeja 
de tipos e os embaralhou para fazer um livro de modelos de tipos.''')


# . Análise
print(frase)
print(len(frase))
print(frase.count('o'))
print(frase.count('O'))
print(frase.count('o', 0, 13))   # count com fatiamento
print(frase.upper().count('O'))

print(frase.find('Curso'))
print(frase.find('Vídeo'))
print(frase.find('vídeo'))
print(frase.lower().find('vídeo'))  # qdo não existe retorn '-1

print('Curso' in frase)  # retornar 'True' ou 'False'


# . Transformação
frase = 'Curso em Vídeo Python'

print(frase.replace('Python', 'Android'))
print(frase)
frase = frase.replace('Python', 'Android')
print(frase)
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())

frase = '   Aprenda Python  '
print(frase)
print(len(frase))
print(len(frase.strip()))
print(len(frase.rstrip()))
print(len(frase.lstrip()))

frase = 'Curso em Vídeo Python'


# . Divisão
frase = 'Curso em Vídeo Python'
print(frase)
print(frase.split())
dividido = frase.split()
print(dividido[0])
print(dividido[1])
print(dividido[2])
print(dividido[2][3])  # obter no dividendo indice '2' que é 'Vídeo', obter o indice '3' que é 'e'


# . Junção
print(dividido)
print('-'.join(dividido))
print(' '.join(dividido))
