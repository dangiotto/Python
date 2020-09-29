d = float(input('Informe a distância em (KM):\n'))
if d <= 200:
    print('Preço da passagem será de R$ {:.2f}'.format(d*0.5))
else:
    print('Preço da passagem será de R$ {:.2f}'.format(d*0.45))