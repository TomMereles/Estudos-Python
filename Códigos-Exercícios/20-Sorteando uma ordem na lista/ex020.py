from random import shuffle
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
alunos = [a1, a2, a3, a4]
#Função shuffle faz com que os elementos da lista sejam embaralhados
shuffle(alunos)
print('A ordem de apresentação será ')
print(alunos)
