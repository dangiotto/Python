n1 = int(input('Informe um número :\n'))
n2 = int(input('Informe outro número :\n'))
n3 = int(input('Informe outro número novamente:\n'))
# verificando quem é menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# verificando o maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O maior número é {}'.format(maior))
print('O menor número é {}'.format(menor))
