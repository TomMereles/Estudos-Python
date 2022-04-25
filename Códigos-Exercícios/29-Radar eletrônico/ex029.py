# Condição simples
vel = int(input('Qual é a velocidade atual do carro? '))
multa = (float(vel - 80) * 7)
if vel > 80:
    print('Multado! Você excedeu o limite permitido que é de 80Km/h')
    print(f'Você deve pagar uma multa de R${multa:.2f} reais')
print('Tenha um bom dia! Dirija com segurança!')
