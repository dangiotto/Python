num = list()
for i in range(0, 5):
    n = int(input('Digite um número :'))
    if i == 0 or n > num[-1]:
        num.append(n)
        print('Número adcionado na última posição')
    else:
        pos = 0
        while pos < len(num):
            if n <= num[pos]:
                num.insert(pos, n)
                print(f'Adicionado na posição {pos}...')
                break
            pos += 1
print('=-='*30)
print(f'Os valores digitados foram {num}')

