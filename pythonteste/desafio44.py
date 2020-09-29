p=float(input('Informe o valor do produto:\n'))
print('=-='*20)
print('SELECIONE UMA DAS CONDIÇÕES DE PAGAMENTO')
print('=-='*20)
print('''[1] à vista - dinheiro/chque - Desconto (10%)
[2] à vista no cartão - Desconto(5%)
[3] em até 2x no cartão - Sem Desconto
[4] 3x ou mais no cartão - Acréscimo (20%)''')
op=int(input('INFORME A OPÇÃO : '))
if op==1:
    print('Preço normal é {:.2f} e com desconto {:.2f}'.format(p,p*0.95))
elif op==2:
    print('Preço normal é {:.2f} e com desconto {:.2f}'.format(p,p*0.9))
elif op==3:
    print('Preço normal é {} e sem desconto com essa forma de pagamento'.format(p))
elif op==4:
    print('Preço normal é {} e parcelado fica {}.'.format(p,p*1.2))