seq =('zero', 'um' , 'dois' , 'três', 'quatro', 'cinco',
      'seis', 'sete', 'oito', 'nove', 'dez' , 'onze' ,
      'doze', 'treze' , 'quatorze', 'quinze', 'dezeseis',
      'dezesete', 'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('Digite um número de 0 a 20 : '))
    if n in range(0,20):
        break
    print('Opção inválida, digite novamente (Entre 0 e 20)')
print(f'Você digitou o número {seq[n]}.')

