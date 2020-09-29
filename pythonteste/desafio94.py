grupo = list ()
mulheres = list()
acimamedia = list()
pessoa = dict()
somaidade = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome : '))
    while True:
        pessoa['sexo'] = str(input('[M/F] : ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Opção inválida [M/F].')
    pessoa['idade'] = float(input('Idade : '))
    grupo.append(pessoa.copy())
    while True:
        opt = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if opt in 'SN':
            break
        print('Erro! Digite S ou N.')
    if opt == 'N':
        break
print('=-='*20)
print(f'- O grupo tem {len(grupo)} pessoas.')
for p, r in enumerate(grupo):
    for k, v in r.items():
        if k == 'idade':
            somaidade += (v)
        if k == 'sexo' and v in 'Ff':         #for p in grupo:
            mulheres.append(grupo[p]['nome']) #    if p['sexo'] in 'fF':
print(f'- A média de idade é {somaidade/len(grupo):.2f} anos')
print(f'- As mulheres cadastradas foram : {mulheres}')     #dentro do if #print(f'p['nome'], end='')
print(f'- Lista de pessoas acima da média : \n')
for p, r in enumerate(grupo):
    for k, v in r.items():
        if k == 'idade' and v > somaidade/len(grupo):
            print(f'{grupo[p]}\n')
print('<<<ENCERRANDO>>>')




