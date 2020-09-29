print('=-='*20)
print('Analisador de Triângulo')
print('=-='*20)

a = float(input('Informe o primeiro lado :'))
b = float(input('Informe o segundo lado: '))
c = float(input('Informe o terceiro lado: '))
if a < b + c and b < a + c and c < a + b:
    print('Pode ser um triângulo')
    if a==b and b==c and c==a:
        print('Tipo Equilatero')
    elif a!=b and b!=c and c!=a:
        print('Tipo Escaleno')
    else:
        print('Tipo Isóceles')
else:
    print('Não pode ser um triângulo')