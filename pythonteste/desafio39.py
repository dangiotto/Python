from datetime import date
a = date.today().year
nasc = int(input('Informe seu ano de nascimento : '))
if (a-nasc) == 18:
    print('Já é hora de se alistar, você tem {} anos.'.format(a-nasc))
elif (a-nasc) > 18:
    print('Já passou {} anos do tempo de alistamento, você tem {} anos.'.format((a-nasc)-18,a-nasc))
else:
    print('Você ainda não tem idade para se alistar, faltam {} anos.'.format(18-(a-nasc)))
