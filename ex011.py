larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
ltinta = area / 2

print('Sua parede tem a dimensão de {}x{} e sua área é de {}m2.'.format(larg, alt, area),
      '\nPara pintar essa parede, você precisará de {}l'. format(ltinta))

