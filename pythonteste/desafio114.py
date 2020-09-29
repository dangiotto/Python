import urllib
from urllib.request import Request, urlopen


try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('Site indisponível')
else:
    print('Site online.')
    print(site.read())
