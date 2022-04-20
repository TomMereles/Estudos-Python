from random import randint
from time import sleep
computador = randint(0, 5) # Faz o computador sortear o número.
print('°-' * 28)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('°-' * 28)
jogador = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no número {} e não no {}!'.format(computador, jogador))