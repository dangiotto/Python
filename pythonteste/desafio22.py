nome = (str(input('Informe seu nome completo: '))).strip()
print('Analisando seu nome...')
print('O nome maiúsculo é : {}'.format(nome.upper()))
print('O nome minúsculo é : {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
separado = nome.split()
print('Seu primeiro nome é {} e tem ao todo {} letras'.format(separado[0], len(separado[0]))) #ou nome.find(' ') primeiro espaço