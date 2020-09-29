geral = list()
nome = list()
notas = list()
while True:
    nome.append(str(input('Digite um nome : ')))         #geral.append([nome, [nota1, nota2], media]) com variáveis
    notas.append(float(input('Digite a nota 1: ')))      #simples no input
    notas.append(float(input('Digite a nota 2: ')))
    nome.append(notas[:])
    geral.append(nome[:])
    notas.clear()
    nome.clear()
    op = str(input('Quer continuar ? [S/N]')).upper().strip()
    while op not in 'NS':
        op = str(input('Opção inválida, quer continuar? [S/N]')).upper().strip()
    if op in 'NS':
        if op == 'N':
            break
print('=-='*15)
print(f'{"Nº"}{"NOME":>6}{"MÉDIA":>15}\n{"-"*25}')
for p, v in enumerate(geral):
    print(f'{p}{v[0]:^13}{(v[1][0]+v[1][1])/2:>8}')
print('-'*25)
while True:
    op = int(input('Mostrar nota de qual aluno? (999 interrompe): '))
    if op == 999:
        break
    else:
        print(geral[op][1])



