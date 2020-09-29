exp = str(input('Digite uma expressão : '))
lista = list()
for simb in exp:                   # Lê letra a letra da exressão
    if simb == '(':                #Verifica existência de '(' na expressão
        lista.append('(')          #inclui '(' na lista
    elif simb == ')':              #Verifica se ')' está na expressão
        if len(lista) > 0:         #Se lista possui mais de um índice (Já recebeu algum valor '(')
            lista.pop()            #O valor '(' é apagado
        else:                      #Se a lista não possuir nenhum índice '(', o valor ')' é adicionado e quebra o loop.
            lista.append(')')
            break
if len(lista) == 0:                #lista sem indice, significa que '(' foi = à ')'.
    print('Sua expressão está válida.')
else:                              #lista com mais de um índice possui '(' e ')' em quantidade diferentes.
    print('Sua expressão está inválida.')

