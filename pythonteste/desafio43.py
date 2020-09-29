a = float(input('Informe a altura (m): '))
p = float(input('Informe o peso : '))
imc=p/(a**2)
if imc < 18.5:
    print('IMC: {:.1f}, Abaixo do peso.'.format(imc))
elif imc>=18.5 and imc<25:
    print('IMC: {:.1f}, Peso Ideal.'.format((imc)))
elif imc>=25 and imc<30:
    print('IMC: {:.1f}, Sobrepeso.'.format(imc))
elif imc>=30 and imc<40:
    print('IMC: {:.1f}, Obesidade.'.format(imc))
else:
    print('IMC: {:.1f}, Obesidade Morbida.'.format(imc))

