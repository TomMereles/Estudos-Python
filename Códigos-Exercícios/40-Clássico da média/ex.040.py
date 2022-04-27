n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
média = (n1 + n2) / 2
print(f'Tirando {n1} e {n2}, a média do aluno é {média:.1f}')
if média >= 6:
    print('O aluno está \033[1;32mAPROVADO\033[m.')
elif média < 5:
    print('O aluno está \033[1;31mREPROVADO\033[m. ')
elif 6 > média >= 5:
    print('O aluno está em \033[1;35mRECUPERAÇÃO\033[m.')
