def notas(*n, sit=False):
    """
    Analisa as notas e situação de vários alunos.
    :param n: uma ou mais notas dos alunos.
    :param sit: Opcional. Apresenta a situação.
    :return: dicionário com várias informações da turma.
    """
    dic={}
    dic['total'] = len(n)
    dic['maior'] = max(n)
    dic['menor'] = min(n)
    dic['media'] = (sum(n)/len(n))
    if sit is True:          #ou if sit:
        if dic['media'] >= 7:
            dic['situação'] = 'BOM!'
        elif dic['media'] >= 5:    #elif já considera a condição anterior.
            dic['situação'] = 'REGULAR!!'
        elif dic['media'] < 5:
            dic['situação'] = 'RUIM!!'
    return dic


resp = notas(3.0, 6, 10, 0, 5.6, sit=True)
print(resp)
help(notas)