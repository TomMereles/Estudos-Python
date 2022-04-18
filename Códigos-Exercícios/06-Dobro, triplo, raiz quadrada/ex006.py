#Cálculo de valores utilizando aritmética com formatação do resultado.
n = int(input('Digite um número: '))
print('O dobro de {} vale {} '.format(n, (n * 2)))
print('O triplo de {} vale {} '.format(n, (n * 3)))
print('A raiz quadra de {} é igual a {:.2f} '.format(n, (n ** (1/2))))
