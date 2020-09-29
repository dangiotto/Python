n = int(input('Digite um número entro 0 e 9999 :'))
u = n // 1 % 10
d = n //10 % 10
c = n //100 % 10
m = n //1000 % 10
print ('''Analisando o número {}
Unidade : {}
Dezena : {} 
Centena : {}
Milhar: {}'''.format(n,u,d,c,m))