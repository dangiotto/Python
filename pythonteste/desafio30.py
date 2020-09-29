from time import sleep
from termcolor import colored
n = int(input('Informe um número:'))
print(colored('Analisando o número....','red'))
sleep(2)
if n % 2 == 0:
    print ('Número {} é par!'.format(n))
else:
    print('Número {} é impar!'.format(n))