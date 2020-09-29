from datetime import datetime
colab = dict()
colab['nome'] = str(input('Nome : ' ))
colab['idade'] = ((datetime.today().year - (int(input('Ano de nascimento : ')))))
colab['ctps'] = int(input('Carteira de Trabalo (0 não tem) : '))
if colab['ctps'] != 0:
    colab['contratacao'] = int(input('Ano de contratação : '))
    colab['aposentadoria'] = colab['idade'] + ((colab['contratacao']+35) - (datetime.now().year))
    colab['salario'] = float(input('Salário : '))
print('=-='*15)
for k, v in colab.items():
    print(f'{k} tem o valor {v}')