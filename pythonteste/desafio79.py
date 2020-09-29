num = list()
while True:
    num.append(int(input('Digite um valor : ')))   #poderia receber o valor em um variável simpler
    if num.count(num[len(num)-1]) != 2:            # verificar se está na lista
        print('Valor adicionado com sucesso...')   # if n not in num: para add ou não
    else:
        num.pop()
        print('Número duplicado, não será adicionado...')
    op = str(input('Quer continuar... [S/N]')).strip().upper()
    if op not in 'NS':
        op = str(input('Opção inválida!!\nQuer continuar... [S/N]')).strip().upper()
    if op == 'N':
        break
num.sort()
print(num)