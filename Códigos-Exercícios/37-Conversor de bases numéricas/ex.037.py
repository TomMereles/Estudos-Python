num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para fazer a conversão:
[1] Converter para BINÁRIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print(f'O número {num} convertido para BINÁRIO é igual a {bin(num)[2:]}')
elif opção == 2:
    print(f'O número {num} convertido para OCTAL é igual a {oct(num)[2:]}')
elif opção == 3:
    print(f'O número {num} convertido para HEXADECIMAL é igual a {hex(num)}')
else:
    print('Opção inválida. Tente novamente.')