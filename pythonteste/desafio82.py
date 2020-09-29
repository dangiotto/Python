num = list()
par = list()
impar = list ()
while True:
    num.append(int(input('Digite um número: ')))
    op = str(input('Quer continuar? [S/N]')).strip().upper()
    if op not in 'SN':
        op = str(input('Opção inválida!\n[S/N] : '))
    if op == 'N':
        break
for i in num:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)
print('=-='*30)
print(f'A lista completa digitada foi {num}.')
print(f'A lista com pares é {par}.')
print(f'A lista de ímpares são {impar}.')