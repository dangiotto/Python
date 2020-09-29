num = list()
while True:
    num.append(int(input('Digite um número: ')))
    op = str(input('Quer continuar? [S/N]')).strip().upper()
    if op not in 'SN':
        op = str(input('Opção inválida!\n[S/N] : '))
    if op == 'N':
        break
print(f'Você digitou {len(num)} elementos.')
num.sort(reverse=True)
print(f'Os valores em ordem decrescente são : {num}.')
if 5 in num:
    print('O valor cinco faz parte da lista')
else:
    print('O valor 5 não faz parte da lista.')

