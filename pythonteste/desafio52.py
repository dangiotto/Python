n = int(input('Informe um número : '))
s = 0
for c in range (1,n+1):
    if n % c == 0:
        s += 1
if s == 2:
    print('É número primo!!')
else:
    print('Não é número primo')