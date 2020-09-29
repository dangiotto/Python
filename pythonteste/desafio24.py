cidade = str(input('Digita o nome da cidade :')).strip()
cidade = cidade.upper().split()
print('A cidade {} começa com SANTO : {}'.format(' '.join(cidade), cidade[0][0:5] == 'SANTO'))