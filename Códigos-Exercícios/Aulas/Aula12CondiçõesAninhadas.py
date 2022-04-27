# Condições Aninhadas: Quer dizer pegar estruturas condicionais e colocar dentro de estruturas condicionais.
nome = str(input('Qual é o seu nome? '))
if nome == 'Tom':
    print('Que nome legal você tem!')
elif nome == 'João' or nome == 'Maria' or nome == 'Paulo' or nome == 'Pedro' or nome == 'Jéssica':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Julia Bianca Caroline Fernanda':
    print('Belo nome feminino.')
else:
    print('Seu nome é bem normal.')
print(f'Tenha um bom dia, \033[32m{nome}\033[m.')