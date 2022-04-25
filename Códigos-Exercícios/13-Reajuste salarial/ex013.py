salario = float(input('Qual é o salário do Funcionário? R$'))
aumento = salario + (salario * 15 / 100)
print(f'Um funcionário que ganhava \033[31mR${salario}\033[m, com \033[1;36m15%\033[m de aumento, passa a receber \033[32mR${aumento:.2f}\033[m')