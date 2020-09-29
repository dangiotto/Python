n1=float(input('Informe a primeira nota : '))
n2=float(input('Informe a segunda nota : '))
m = (n1+n2)/2
if m < 5:
    print('Média {:.1f}, abaixo de 5: Reproved'.format(m))
elif 6.9 >= m >= 5:
    print('Média {:.1f}, entre 5.0 e 6.9: Recuperation'.format(m))
else:
    print('Média {:.1f}, igual ou superior à 7.0: Aprovado'.format(m))