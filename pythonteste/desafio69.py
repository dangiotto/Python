from termcolor import colored
maior18 = homens =mulher20 =0
while True:
    idade =int(input('Digite a idade : '))
    sexo =str(input('Digite o sexo: [M/F]')).strip().upper()
    if sexo not in 'MF':
        print(colored('Sexo inválido\nDigite novamente!', 'red'))
        sexo = str(input(colored('Digite o sexo: [M/F]','yellow'))).strip().upper()
    if sexo == 'M':
        homens += 1
    if idade > 18:
        maior18 += 1
    if sexo == 'F' and idade < 20:
        mulher20 += 1
    op = str(input('Deseja continuar ? [S/N]')).strip().upper()
    if op not in 'SN':
        print(colored('Opção inválida digite novamente', 'red'))
        op = str(input(colored('Deseja continuar ? [S/N]', 'yellow'))).strip().upper()
    if op == 'N':
        print(f'Pessoas com mais de 18 anos: {maior18}')
        print(f'Quantidade de homens: {homens}')
        print(f'Quantidade de mulheres com menos de 20 anos: {mulher20}')
        break