n=int(input('Informe um número : '))
print('''ESCOLHA UMA DAS BASES PARA CONVERSÃO : 
[1] Converter para BINÁRIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL''')
op=(int(input('Seleciona a sua opção : ')))
if op == 1:
    print('Conversão de {} em binários é : {}'.format(n,bin(n)[2:]))
elif op == 2:
    print('Conversão de {} em octal é : {}'.format(n,oct(n)[2:]))
elif op == 3:
    print('Conversão de {} em Hexa é : {}'.format(n,hex(n)[2:]))
else:
    print('Opção Inválida')