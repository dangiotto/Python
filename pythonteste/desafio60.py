'''n =int(input('Informe um número : '))
c = n
f = 1
while c > 0:
    print('{} '.format(c), end='')
    print('x ' if c > 1 else '= ', end='')
    f *= c
    c -= 1
print('{}'.format(f))'''
f = 1
n = int(input('Informe um número : '))
for c in range (n,0,-1):
    print('{}'.format(c),end='')
    print(' x ' if c > 1 else ' = ',end='')
    f *= c
print('{}'.format(f), end='')
    #f *= (n*c)
#print('= {}'.format(f))



#from math import factorial
#n =int(input('Informe um número'))
#f = factorial(n)
#print('Fatorial de {} é {}'.format(n, f))