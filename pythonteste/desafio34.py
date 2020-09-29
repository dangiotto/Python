sal = float(input('Qual o seu salário ?\nR$: '))
if sal <= 1250:
    nsal = sal*1.15
else:
    nsal = sal*1.1
print('Novo salário é {:.2f}'.format(nsal))