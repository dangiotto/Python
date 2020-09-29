while True:
    v = int(input('Quer ver a tabuada de qual valor? '))
    if v < 0:
        break
    print('-'*40)
    for i in range (1,11):
        m= v * i
        print(f'{v} X {i} = {m}')
    print('-'*40)
print('Fim da Tabuada do Gizé')