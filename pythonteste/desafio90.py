dic = dict()
dic['nome'] = str(input('Nome : '))
dic['média'] = float(input(f'Qual a média de {dic["nome"]}? '))
if dic['média'] >= 7:
    dic['sit'] = 'Aprovado'
elif 5.5 >= dic['média'] < 7:
    dic['sit'] = 'Recuperação'
else:
    dic['situação'] = 'Reprovado'
for k, v in dic.items():
    print(f'{k.capitalize()} é igual a {v}.')
