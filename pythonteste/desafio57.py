somaidade = 0
maioridadehomen = 0
nomevelho = ''
totmulher20 = 0
for c in range(0, 4):
    print('---- {}ª Pessoa -----'.format(c+1))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().lower()
    while sexo not in 'mf':
        print('Opção Inválida! Digite novamente')
        sexo = str(input('Sexo [M/F]: ')).strip().lower()
        if sexo == 'm' or sexo == 'f':
            somaidade += idade
            if c == 1 and sexo in 'Mm':
                maioridadehomen = idade
                nomevelho = nome
            if sexo in 'Mm' and idade > maioridadehomen:
                maioridadehomen = idade
                nomevelho = nome
            if sexo in 'Ff' and idade < 20:
                totmulher20 += 1
médiaidade = somaidade / 4
print('A média de idade do grupo é de {:.0f} anos.'.format(médiaidade))
print('A idade do homem mais velho é {} e ele se chama {}.'.format(maioridadehomen,nomevelho))
print('Existem {} mulheres com menos de 20 anos.'.format(totmulher20))