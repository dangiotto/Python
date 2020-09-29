num = list()
for i in range(0, 5):
    num.append(int(input(f'Digite um número para a posição {i}: ')))
print('=-='*30)
print(f'Você digitou os valores {num}.')
print(f'O maior valor digitado foi {max(num)} na posição', end=' ')
for c, v in enumerate(num):
    if v == max(num):
        print('{:.<3}'.format(c),end=' ')
print(f'\nO menor valor digitado foi {min(num)} na posição', end= ' ')
for c, v in enumerate(num):
    if v == min(num):
        print('{:.<3}'.format(c),end=' ')
