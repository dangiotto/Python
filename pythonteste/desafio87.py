matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = soma3col = maior2l  = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]:'))
print('=-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]',end='')
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
        if c == 2:
            soma3col += matriz[l][c]
        if l == 1 and c ==0:
            maior2l = matriz[l][c]
        if l ==1 and c > 0 and matriz[l][c] > maior2l:
            maior2l = matriz[l][c]
    print()
print('=-='*30)
print(f'A soma dos números pares são {somapar}.')
print(f'A soma dos valores da terceira coluna é : {soma3col}.')
print(f'O maior número da segunda linha é {maior2l}.')