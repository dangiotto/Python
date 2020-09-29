from random import shuffle
n = []
for i in range (0,4):
    n.append(str(input('Informe o nome dos alunos :')))
shuffle(n)
print (n)