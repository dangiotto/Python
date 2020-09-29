palavras = ('aprender', 'programar', 'linguagem',
           'python', 'curso', 'gratis', 'estudar',
           'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for c in range (0, len(palavras)): #for p in palavras
    letra = str(palavras[c]).upper()
    print(f'\nNa palavra {palavras[c].upper()} temos as vogais ', end='')
    for i in range (0, len(letra)): #for letra in c:
        if letra[i] in 'AEIOU':     #  if letra in 'AEIOU'
            print(f'{letra[i].lower()} ', end='')

