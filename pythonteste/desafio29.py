from termcolor import colored
v = int(input('Qual a velocidade do veículo?\n'))
if v <= 80:
    print(colored('Dentro da velocidade permitida','blue'))
else:
    print(colored('Você foi multado em {:.2f} reais!!','red').format((v-80)*7))