print('--' * 20)
print('\033[1m\033[4mAnalisador de Triângulos\033[m')
print('--' * 20)
a = float(input('\033[1mPrimeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    print('\033[mOs segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')