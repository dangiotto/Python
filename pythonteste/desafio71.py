print('='*30)
print ('{:^30}'.format('BANCO CEV'))
print('='*30)
cedula = 0
resto = 0
while True:
    saque =int(input('Qual valor quer sacar ? R$'))
    if saque >= 50:
        cedula = int(saque/50)
        saque -= (cedula*50)
        print(f'{cedula} cédulas de R$ 50.')
    if saque >= 20:
        cedula = int(saque/20)
        saque -= (cedula * 20)
        print(f'{cedula} cédulas de R$ 20.')
    if saque >= 10:
        cedula = int(saque/10)
        saque -= (cedula * 10)
        print(f'{cedula} cédulas de R$ 10.')
    if saque >= 1:
        cedula = int(saque/1)
        print(f'{cedula} cédulas de R$ 1.')
    print('='*30,'\nVOLTE SEMPRE AO BANCO CEV\n','='*30)









