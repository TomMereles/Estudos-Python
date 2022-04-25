from random import randint
from time import sleep
computador = randint(0, 5) # Faz o computador sortear o número.
print('\033[1;31m-°-\033[m' * 18)
print('\033[1mVou pensar em um número entre 0 e 5. Tente advinhar...\033[m')
print('\033[1;31m-°-\033[m' * 18)
jogador = int(input('\033[4;35mEm que número eu pensei?\033[m ')) # Jogador tenta adivinhar
print('\033[1;35mPROCESSANDO...\033[m')
sleep(2)
if jogador == computador:
    print('\033[32mPARABÉNS!\033[m Você conseguiu me vencer!')
else:
    print(f'\033[32mGanhei!\033[m Eu pensei no número \033[1;32m{computador}\033[m e não no \033[1;31m{jogador}\033[m!')