from random import choice
a1 = input('\033[1;32mPrimeiro aluno:\033[m ')
a2 = input('\033[1;33mSegundo aluno:\033[m ')
a3 = input('\033[1;34mTerceiro aluno:\033[m ')
a4 = input('\033[1;35mQuarto aluno:\033[m ')
alunos = [a1, a2, a3, a4]
#Função choice retorna um elemento da sequência sorteada.
escolhido = choice(alunos)
print(f'O aluno escolhido foi \033[7;31m{escolhido}\033[m')
