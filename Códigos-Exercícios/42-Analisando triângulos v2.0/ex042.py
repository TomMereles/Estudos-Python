r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if r1 == r2 == r3:
        print('\033[32mEQUILÁTERO\033[m!')
    elif r1 != r2 != r3 != r1:
        print('\033[31mESCALENO\033[m!')
    else:
        print('\033[34mISÓSCELES\033[m!')
else:
    print('\033[1mOs segmentos acima NÃO PODEM FORMAR triângulo\033[m')
