from ast import Num


num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Analisando o número {num}')
print(f'Unidade: {u}'.format(u))
print(f'Dezena: {d}'.format(d))
print(f'Centena: {c}'.format(c))
print(f'Milhar: {m}'.format(m))
