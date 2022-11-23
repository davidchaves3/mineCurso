import re

linha_erro = []
regex = "[a-zA-Z]{3}[0-9]{6}\s{2}[a-zA-Z][0-9]{8}\s{4}[a-zA-Z]{2}[0-9]{32}"

with open('boletos-importacao.txt','r') as b:
  boletos =b.readlines()
  [linha_erro.append(boletos.index(x)) for x in boletos if not re.findall(regex,x)]

print(linha_erro)