salário = float(input('Qual o salário do funcionário? R$'))
aumentoMaior = salário + (salário * 15 / 100)
aumentoMenor = salário + (salário * 10 / 100)
if salário <= 1250:
    print(f'Quem ganhava R${salário:.2f} passa a ganhar R${aumentoMaior:.2f} agora.')
else:
    print(f'Quem ganhava R${salário:.2f} passa a ganhar R${aumentoMenor:.2f} agora.')

