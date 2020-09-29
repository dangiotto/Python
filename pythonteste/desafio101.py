def voto(a):
    from datetime import datetime
    idade = (datetime.now().year) - a
    if idade < 18:
        return print(f'Com {idade} anos: NAO VOTA')
    elif 65 >= idade >= 18:
        return print(f'Com {idade} anos: VOTO OBRIGATÓRIO!')
    else:
        return print(f'Com {idade} anos: VOTO OPCIONAL!')


print('-'*30)
ano = int(input('Type your year of bithday : '))
voto(ano)