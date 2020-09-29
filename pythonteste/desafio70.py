barato = soma = mil = 0
nomebarato = ''
while True:
    nome =str(input('Digite o nome do produto: ')).upper().strip()
    preco =float(input('Digite o preço :'))
    op = str(input('Deseja cadastrar outro produto? : [S/N]')).upper().strip()
    barato = preco
    nomebarato = nome
    soma += preco
    if preco < barato:
        barato = preco
        nomebarato = nome
    if preco > 1000:
        mil += 1
    while op not in 'SN':
        print('Opção inválida, digite novamente!')
        op = str(input('Deseja cadastrar outro produto? : [S/N]')).upper().strip()
    if op == 'N':
        break
print(f'Total de gastos é R$ {soma}.')
print(f'{mil} produtos custam mais de R$ 1.000.')
print(f'O produto mais barato é {nomebarato}, e custa R$ {barato}.')

