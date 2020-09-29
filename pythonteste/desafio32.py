from datetime import date
ano = int(input('Informe o ano ou coloque 0 para anlisar o ano atual:\n'))
if ano == 0:
    ano = date.today().year
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print('O ano {}, é bisexto'.format(ano))
else:
    print('O ano {}, não é bisexto'.format(ano))