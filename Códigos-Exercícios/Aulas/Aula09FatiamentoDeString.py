# ************** Fatiamento de string *******************

frase = 'Tom Mereles'
print(frase[9])  # Pega a letra 'e' final, indice dentro da string(frase).

print(frase[4:11])  # Pega apartir do 'M' e vai até o 's'.

# Pega apartir de 'm' e vai até o final pulando de 2 em 2 caracters.
print(frase[2:11:2])

# Contando apartir de 0 vai pegar o caracter de 0(T) até o 3(espaço em branco).
print(frase[:3])

# Pega apartir do 'r' que é o caracter onde esta localizado a 6° posição de frase e imprime até o final.
print(frase[6:])

# Pega a letra 'M' até o final, pulando de 3 em 3 caracters.
print(frase[4::3])


# >>>>>>>>>>>>>>>>> Análise de string <<<<<<<<<<<<<<<<<<<<<

# Mostra o comprimento da frase
print(len(frase))

# Conta quantas vezes aparece a letra 'e' minúscula na variável frase.
print(frase.count('e'))

# Conta quantas vezes aparece a letra 'e' minúscula já com fatiamento.
print(frase.count('e', 4, 8))

# Mostra apartir de que posição iniciou determinados caracteres da palavra.
print(frase.find('Mer'))

# Caso não exista o caracter ou palavra retornara -1 que significa que não existe tal caracter ou palavra na string.
print(frase.find('Campos'))

# Existe Tom in frase, caso exista retornara true.
print('Tom' in frase)


# >>>>>>>>>>>>>>>>> Transformação <<<<<<<<<<<<<<<<<<<<<

# Irá substituir uma palavra por outra.
print(frase.replace('Mereles', 'Campos'))

# Método para deixar todas as letras maiúsculas.
print(frase.upper())

# Método para deixar todas as letras minúsculas.
print(frase.lower())

# Método para deixar apenas o primeiro caracter de uma frase em maiúsculo.
print(frase.capitalize())

# Método para deixar a primeira letra das palavras separadas por espaço em maiúscula.
print(frase.title())

# Nova variável declara para utilizar como exemplo das demais transformações.
frase2 = '   Eu sou o Tom Mereles     '

# Remove todo espaço do ínicio e fim da frase ou string e a contagem de caracteres volta ao normal iniciando por 0.
print(frase2.strip())

# Remove todos os espaços do lado direito da frase ou string.
print(frase2.rstrip())

# Remove todos os espaços do lado esquerdo da frase ou string.
print(frase2.lstrip())


# >>>>>>>>>>>>>>>>> Divisão <<<<<<<<<<<<<<<<<<<<<

# Divide uma string em uma lista, onde cada string dentro da lista inicia seu indice em 0.
print(frase.split())


# >>>>>>>>>>>>>>>>> Junção <<<<<<<<<<<<<<<<<<<<<

# Após dividir ou ter uma string transformada pelo split, usa o join para unir ela novamente.
print('-'.join(frase.split()))


# print para escrever um texto na tela sem precisar usar vários prints por linha.
print('''\nOlá, tudo bem?
Aqui esta o exemplo de que podemos escrever várias linhas,
utilizando o mesmo print!\n''')