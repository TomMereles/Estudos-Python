from datetime import date
sexo = (input('\033[1mSeja bem vindo(a) ao alistamento Militar\033[m! \nAperte \033[32mENTER\033[m para continuar: '))
print('''Você é:
\033[1m[1]\033[m \033[35mMulher\033[m
\033[1m[2]\033[m \033[36mHomem\033[m''')
opção = int(input('Digite uma das opções: '))
if opção == 1:
    print('\033[4;32mVocê não precisa fazer alistamento militar obrigatório! \nTenha um ótimo dia.\033[m')
else:
    print('Olá, tudo bem?\n')
    nasc = int(input('\033[1mQual é o seu ano de nascimento:\033[m '))
    atual = date.today().year
    idade = atual - nasc
    print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}.')
    if idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE!')
    elif idade < 18:
        saldo = 18 - idade
        ano = atual + saldo
        print(f'Ainda faltam {saldo} anos para o alistamento. \nSeu alistamento será em {ano}.')
    else:
        saldo = idade - 18
        ano = atual - saldo
        print(f'Você já deveria ter se alistado há {saldo} anos. \nSeu alistamento foi em {ano}.')
