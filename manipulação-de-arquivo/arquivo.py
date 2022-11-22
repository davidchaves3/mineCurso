#Manipulação de arquivos 

arquivo = open('arquivo.txt','a', encoding='uft-8')
 # Se o arquivo não existe, o python vai criar um.

frases = list()
frases.append('Minicurso\n')
frases.append('Python\n')
frases.append('Olá mundo\n')

arquivo.writelines(frases) 
arquivo.close()#Sempre fecha o arquivo

