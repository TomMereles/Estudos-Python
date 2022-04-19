frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra {} apareceu {} vezes na frase.'.format(
    frase[0], frase.count('A')))
print('A primeira letra {} apareceu na posição {}'.format(
    frase[0], frase.find('A')))
print('O ultimo {} aparece na posição {}.'.format(frase[0], frase.rfind('A')))
