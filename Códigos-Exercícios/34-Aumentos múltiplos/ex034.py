salário = float(input('Qual o salário do funcionário? R$'))
aumentoMaior = salário + (salário * 15 / 100)
aumentoMenor = salário + (salário * 10 / 100)
if salário <= 1250:
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salário, aumentoMaior))
else:
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salário, aumentoMenor))

