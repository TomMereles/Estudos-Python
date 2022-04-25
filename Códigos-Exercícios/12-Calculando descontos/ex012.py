preço = float(input('\033[1mQual o preço do produto? R$\033[m'))
novo = preço - (preço * 5 / 100)
print(f'O produto que custava \033[1;31mR${preço:.2f}\033[m, na promoção com desconto de 5% vai custar \033[1;32mR${novo:.2f}\033[m.')