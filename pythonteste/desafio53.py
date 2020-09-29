frase = str(input('Digite uma frase : ')).lower().strip().replace(' ','')
letras = list(frase) #depois de splitar FRASE poderia fazer um ''.join(frase)
inv = letras[::-1]       #for letra in range (len(letras) -1, -1, -1) Lê as letras de forma inversa
if letras == inv:        #inv += letras[letra]       'letras' é uma string com as letras juntas
    print('É palíndrono!')
else:
    print('Não é palíndrono!')

