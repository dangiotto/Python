dados = list()
lista = list()
pesado = list()
leve = list ()
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso : ')))
    if len(lista) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    lista.append(dados[:])
    dados.clear()
    op = str(input('Quer continuar ?[S/N]'))
    while op not in 'NnsS':
        print('Opção inválida!')
        op = str(input('Quer continuar ?[S/N]'))
    if op in 'nN':
        break
#for p, v in enumerate(lista):       Substituido pela linha 9 a 15
#    if p == 0:
#        maior = v[1]
#        menor = v[1]
#    if p > 0:
#        if v[1] > maior:
#           maior = v[1]
#        if v[1] < menor:
#            menor = v[1]
#for p in lista:
#    if p[1] == maior:
#        pesado.append(p[0])
#    if p[1] == menor:
#        leve.append(p[0])
print('=-='*30)
print(f'Você cadastrou {len(lista)} pessoas.')
print(f'O menor peso foi {menor} KG. Peso de ', end='')
for p in lista:
    if p[1] == menor:
        print(f'{p[0]}', end='')
print(f'\nO maior peso foi {maior} KG. Peso de ', end='')
for p in lista:
    if p[1] == maior:
        print(f'{p[0]}', end='')






