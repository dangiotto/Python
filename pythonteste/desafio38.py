from time import sleep
n1 = int(input('Infomrme o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
print('Analisando números....')
sleep(2)
if n1 > n2:
    print ('O primeiro número ({:.1f}) é maior que o segundo ({:.1f})'.format(n1,n2))
elif n2> n1:
    print('O segundo número ({}) é maior que o primeiro ({})'.format(n2,n1))
else:
    print('Não há número maior, {} é igual à {}.'.format(n1,n2))