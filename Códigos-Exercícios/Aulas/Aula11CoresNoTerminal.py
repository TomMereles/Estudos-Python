# Código de cores no terminal
# 0 No exemplo é o estilo da fonte(Style)
# 0 None,
# 1 Bold,
# 4 Underline,
# 7 negative(Inverte a cor de fundo com a cor do texto).

# 33 No exemplo é cor do texto(Text)
# 30 branco,
# 31 vermelho,
# 32 verde,
# 33 amarelo,
# 34 azul,
# 35 magenta,
# 36 ciano,
# 37 cinza(cor padrão).

# 44 No exemplo é a cor de fundo (Back)
# 40 branco,
# 41 vermelho,
# 42 verde,
# 43 amarelo,
# 44 azul,
# 45 magenta,
# 46 ciano,
# 47 cinza.
# >>>>>>>EXEMPLO<<<<<<<<
# \033[0;33;44m

# a = 3
# b = 9
# print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))

# nome = 'Tom'
# print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))

nome = 'Tom'
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;37m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(
    cores['pretoebranco'], nome, cores['limpa']))
