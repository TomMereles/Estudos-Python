real = float(input('\033[1mQuanto de dinheiro você tem na carteira? R$\033[m'))
dolar = real / 3.27
print(f'Com\033[1;32m R${real:.2f}\033[m você pode comprar\033[1;32m US${dolar:.2f}\033[m!')
