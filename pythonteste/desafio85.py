num = list() # lista dentro de lista num = [[], []]
impar = list()
par = list ()
num.append(par)
num.append(impar)
for c in range (0, 7):
    n = int(input(f'Digite o {c+1}º valor: '))
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram {num[0]}.')
print(f'Os valores ímpares digitados foram {num[1]}.')