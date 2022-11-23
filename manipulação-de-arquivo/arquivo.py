#Manipulação de arquivos 

arquivo = open('arquivo.txt','a', encoding='utf-8')
 # Se o arquivo não existe, o python vai criar um.

#Adicionar ao arquivo
frases = list()
frases.append('Minicurso\n')
frases.append('Python\n')
frases.append('Olá mundo\n')

arquivo.writelines(frases)
arquivo.close()#Sempre fecha o arquivo

#Ler o arquivo
arquivo = open('arquivo.txt','a', encoding='utf-8')
print(arquivo.read())
print(arquivo.readline(5)) # Vai trazer a posição 5 que está no arquivo
arquivo.close()

