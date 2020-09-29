from datetime import date
maior = 0
menor = 0
for c in range(0,7):
    ano = int(input('Informe o ano de nascimento :'))
    if (date.today().year - ano) < 18:
        menor += 1
    else:
        maior += 1
print('{} pessoas são de maior e {} são de menor.'.format(maior,menor))
