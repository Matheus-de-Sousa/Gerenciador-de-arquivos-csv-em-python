"""
Gerador e gerenciador de arquivos csv

Esse programa tem o objetivo de permitir que o usúario crie e edite um arquivo csv
para utilizá-lo, principalmente, como um datalogger ou em uma planilha do excel.

O que são arquivos csv(comma-separated values)?

O CSV é uma implementação particular de arquivos de texto separados por um delimitador, 
que usa a vírgula e a quebra de linha para separar os valores. O formato também usa as 
aspas em campos no qual são usados os caracteres reservados (vírgula e quebra de linha). 
Essa robustez no formato torna o CSV mais amplo que outros formatos digitais do mesmo 
segmento.
"""
opc='s' #Diz se o usuário deseja continuar o programa
while opc == 's':
    #Opções que o programa oferece
    print('1 - Exibir dados da tabela csv')
    print('2 - Deletar registro')
    print('3 - Adicionar registro')
    print('4 - Buscar registro')
    print('5 - Gerar arquivo csv')
    esc = int(input('')) #Escolha do usuário
    while esc >5 or esc<1: #Verifica se o usuário fez uma escolha válida
        esc = int(input('Opçāo inválida digite outra opçāo:'))
    if esc == 1: #imprime os registros
        arq = open('dbcsv.csv','r')
        registros = arq.readlines() #Lê e armazena todas as linhas do arquivo csv em uma lista(cada linha como um elemento)
        arq.close()
        #Imprime os registros do arquivo csv formatados e alinhados
        commafound = True #variável que verifica se a lista registros ainda possui elementos com vírgula
        while(commafound):
            commapos = 0 #Index da posição da vírgula no registro onde a vírgula está na maior posição em relação aos outros registros
            commafound = False
            #Verifica se os registros possuem vírgulas e atualiza commapos para o index da posição da vírgula de um dos registros
            for registro in registros:
                if registro.find(',') != -1 and commapos < registro.find(','):
                    commafound = True
                    commapos = registro.find(',')
            #------------------------------------------------------------------------------
            if not commafound: break #Checa se algum registro ainda possui vírgulas e se não sai do while
            #Coloca a vírgula de todos os registros no mesmo index, preenchendo os índices vazios com espaço, por fim substitue as vírgulas por uma barra reta
            for i in range(len(registros)):
                registro = registros[i]
                if registros[i].find(',') !=-1 and registros[i].find(',') < commapos:
                    registro = registro[0:registro.find(','):1] + (' '*(commapos-registro.find(','))) + registro[registro.find(',')::]
                registro = registro.replace(',','|',1)
                registros.pop(i) 
                registros.insert(i,registro)
            #-------------------------------------------------------------------------------
        for registro in registros: # imprime todos os registros
            registro = registro.replace(',','|')
            print(registro,end='')
        #---------------------------------------------------------------------------------
    if esc == 2 or esc == 4: #Busca ou deleta registros
        arq = open('dbcsv.csv','r')
        registros = arq.readlines()
        arq.close()
        regprint = registros.copy() #Variável para trabalhar na formatação dos registros
        chaves = registros[0] #Chaves da tabela csv
        chaves = chaves.split(',') #Cada chave se transforma no elemento de uma lista
        for i in range(len(chaves)): 
            chaves[i] = chaves[i].lower()
            chaves[i] = chaves[i].replace('\n','')
        registros.pop(0) #retira as chaves da lista registros
        for i in range(len(registros)): registros[i] = registros[i].lower().split(',') #Os registros são separados em chaves(sendo cada chave o elemento de uma lista) e transformados em minúsculos
        chave = input('Digite o nome da chave que será utilizada para a busca do registro:')
        chave = chave.lower()
        while not (chave in chaves):
            chave = input('Digite o nome da chave que será utilizada para a busca do registro:')
            chave = chave.lower()
        chavepos = chaves.index(chave) #Posição da chave que será utilizada na busca dos registros
        regfound = False #Variável que indica se o(s) registros foram encontrados
        if esc == 2: #Deleta um registro
            item = input('Digite o nome do item que quer deletar:').lower()
            #Deleta um registro e atualiza o arquivo csv, além de imprimir o registro que foi deletado
            for i in range(len(registros)):
                registro = registros[i]
                if registro[chavepos].replace('\n','') == item:
                    regfound = True
                    strprint = regprint.pop(i+1).replace(',','|')
                    strprint = strprint.replace('\n','')
                    print(strprint + ' - Registro deletado')
                    arq = open('dbcsv.csv','w')
                    for regp in regprint: arq.write(regp)
                    arq.close()
                    break
            #------------------------------------------------------------------------------
        else: #Pesquisa registros
            item = input('Digite o nome do item que quer pesquisar:').lower()
            for i in range(len(registros)): #Busca os registros e os imprime na tela
                registro = registros[i]
                if registro[chavepos].replace('\n','') == item:
                    regfound = True
                    print(regprint[i+1].replace(',','|'))
                    
        if regfound: print('Registro localizado com sucesso')
        else: print('Nenhum registro com esse item foi encontrado')
    if esc == 3: #Adiciona registros no arquivo csv
        arq = open('dbcsv.csv','r')
        chaves= arq.readline().split(',') #Chaves separadas em uma lista
        arq.close()
        print('Digite o nome dos itens das chvaves sem o uso de vírgulas e nem aspas')
        arq = open('dbcsv.csv','a')
        nome_chave = input("Digite o/a " + chaves[0].replace('\n','') + ":") # Nome do item da chave
        nome_chave = nome_chave.replace(',','')
        nome_chave = nome_chave.replace("'",'')
        nome_chave = nome_chave.replace('"','')
        arq.write(nome_chave)
        chaves.pop(0) #Remove a primeira chave
        for chave in chaves: #Pede ao usuário o nome dos itens do resto das chaves e adiciona os itens ao arquivo csv
            nome_chave = input("Digite o/a " + chave.replace('\n','') + ":")
            nome_chave = nome_chave.replace(',','')
            nome_chave = nome_chave.replace("'",'')
            nome_chave = nome_chave.replace('"','')
            arq.write(',')
            arq.write(nome_chave)
        arq.write('\n')
        arq.close()
    if esc == 5: #Cria um arquivo csv
        print('Digite as chaves do banco de dados(sem utilizar aspas e nem vírgulas)')
        arq = open('dbcsv.csv','w')
        chave = input('Digite o nome da chave:')
        chave = chave.replace(',','')
        chave = chave.replace("'",'')
        chave = chave.replace('"','')
        arq.write(chave)
        opcdb = input('Deseja criar mais chaves S/N? ').strip().lower()
        while opcdb == 's': #Pede o nome das chaves da tabela csv e as adiciona ao arquivo
            arq.write(',')
            chave = input('Digite o nome da chave:')
            chave = chave.replace(',','')
            chave = chave.replace("'",'')
            chave = chave.replace('"','')
            arq.write(chave)
            opcdb = input('Deseja criar mais chaves S/N? ').strip().lower()
        arq.write('\n')
        arq.close()
    opc = input('Deseja continuar o programa S/N? ').strip().lower()