sal = float(input('Informe sua renda :'))
casa = float(input('Informe o valor do imóvel proposto :'))
prazo = int(input('Qual o prazo do financiamento em meses :'))
parcela = (casa/prazo)
if parcela > (sal*0.3):
    print('Financiamento reprovado, parcela de {:.2f} é maior que 30% da renda ({:.2f}) !!'.format(parcela,sal*0.3))
else:
    print('Emprestimo aprovado, parcela de {:.2f} é menor que 30% da renda ({:.2f}) !!'.format(parcela,sal*0.3))