larg = float(input('\033[1mLargura da parede:\033[m '))
alt = float(input('\033[1mAltura da parede:\033[m '))
area = larg * alt
ltinta = area / 2

print(f'Sua parede tem a dimensão de \033[1;31m{larg}\033[m x \033[1;31m{alt}\033[m e sua área é de \033[1;32m{area}m2\033[m.'
      f'\nPara pintar essa parede, você precisará de \033[1;37m{ltinta}\033[m litros de tinta.')

