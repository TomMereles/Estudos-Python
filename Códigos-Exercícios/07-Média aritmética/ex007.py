# Média de notas, somando e dividindo o resultado total da soma.
n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
m = float(n1 + n2) / 2
print(f'A média entre {n1} e {n2} é igual a {m:.1f} ')
if m >= 6:
    print(f'Parabéns, você tirou {m} e passou!')
else:
    print(f'Sinto muito, você tirou {m} e não passou, estude mais da próxima vez!')
