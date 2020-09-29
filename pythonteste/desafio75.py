n =(int(input('Digite um número: ')), int(input('Digite outro número: ')),
    int(input('Digite mais um número: ')), int(input('Digite o último número: ')))
print(f'Você digitou os números: {n}')
print(f'O valor 9 aparece {n.count(9)} vezes')
if 3 in n:
    print(f'O valor 3 apareceu na posição {n.index(3)+1}')
else:
    print('O valor 3 não foi digitado.')
print('Os valores pares são : ', end='')
for c in n:
    if c % 2 == 0:
        print(f'{c}', end= ' ')
