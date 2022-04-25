frase = str(input('Digite uma frase: ')).strip().upper()
vezes = frase.count('A')
# Acrescentei + 1 para melhor visualização do usuário.
primeira = frase.find('A') + 1
ultima = frase.rfind('A')
print(f'A letra {frase[0]} apareceu {vezes} vezes na frase.')
print(f'A primeira letra {frase[0]} apareceu na posição {primeira}')
print(f'O ultimo {frase[0]} aparece na posição {ultima}.')
