c = 1
f = 0
t1 =0
t2 =1
print('-'*5,'SEQUENCIA DE FIBONACCI','-'*5)
q = int(input('Qual quantidade de elementos quer visualizar? '))
print('{} -> {}'.format(t1,t2), end='')
cont = 3
while cont <= q:
    t3 = t1 + t2
    print('-> {}'.format(t3), end='')
    t1= t2
    t2 =t3
    cont += 1
print('\nFIM')