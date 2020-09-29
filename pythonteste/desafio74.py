from random import randint
maior = menor = maiorant = 0
menorant = 10
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram :', n)
menorant = 10
#for c in range (0,5): #for c in n:
 #   maior = n[c]
  #  menor = n[c]
   # if maior > maiorant:
    #    maiorant = maior
    #if menor < menorant:
    #    menorant = menor
#print(f'O maior número é {maiorant} e o menor é {menorant}.')
print(f'O maior valor foi {max(n)}.')
print(f'O menor valor foi {min(n)}.')