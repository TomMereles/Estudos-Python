# a = int(input('Primeiro valor: '))
# b = int(input('Segundo valor: '))
# c = int(input('Terceiro valor: '))
# Verificando quem é o menor
# menor = a
# if b < a and b < c:
#     menor = b
# if c < a and c < b:
#     menor = c
# Verificando quem é o maior
# maior = a
# if b > a and b > c:
#     maior = b
# if c > a and c > b:
#     maior = c
# print('O menor valor digitado foi {}'.format(menor))
# print('O maior valor digitado foi {}'.format(maior))


n1 =int(input('digite o primeiro número:  '))
n2 =int(input('Digite o segundo número: '))
n3 =int(input ('Digite o terceiro número: '))

lista =[n1,n2,n3]
lista_ordenada = sorted(lista)

print('O menor número é {}'.format(lista_ordenada[0]))
print ('O maior número é {}'.format(lista_ordenada[2]))