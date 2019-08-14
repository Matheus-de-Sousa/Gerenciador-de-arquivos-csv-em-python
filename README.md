# Gerenciador de arquivos csv em python
O objetivo do programa é permitir que o usuário crie tabelas csv e também que busque, visualize, adicione ou delete registros de uma tabela csv, podendo utilizá-la como datalogger ou no excel.


## O que são arquivos csv(comma-separated values)?

O CSV é uma implementação particular de arquivos de texto separados por um delimitador, que usa a vírgula e a quebra de linha para separar os valores. 
O formato também usa as aspas em campos no qual são usados os caracteres reservados (vírgula e quebra de linha). Essa robustez no formato torna o CSV mais 
amplo que outros formatos digitais do mesmo segmento.


## Funcionamento

Este programa foi criado em python 3 e funciona oferecendo opções ao usuário relacionadas com o gerenciamento de um arquivo csv 
como: visualizar, adicionar, deletar ou buscar registros de uma tabela csv. Para escolher uma das opções basta digitar no teclado o número correspondente a ela e pressionar enter.
  
   Após a escolha de uma das opções o programa pedirá ao usuário as informações necessárias para prosseguir,por exemplo, o que ele deseja pesquisar, nome da chave que quer inserir na tabela, nome do item que deseja deletar, etc. Com isso o programa pode continuar, exibindo informações pertinentes ao usuário e atualizando o arquivo csv se necessário.
   
  Porém primeiramente o usuário deve se certificar de que na pasta onde está o programa existe um arquivo com o nome "dbcsv.csv", pois é esse o arquivo que o programa vai utilizar para salvar e ler os dados da tabela csv, esse arquivo pode ser criado no próprio programa na opção "Gerar arquivo csv" ou criado manualmente e salvo com o nome "dbcsv" e extensão ".csv", caso esse arquivo não exista o programa pode exibir um erro, dependendo do que seja solicitado à ele. 

## Como usar


Abra o programa bdcsv.py em um interpretador do python 3 e execute o código, serão exibidas 5 opções que poderão ser escolhidas digitando
o número delas no teclado e pressionando enter. Mas antes de escolher alguma opção gere o arquivo csv de nome "dbcsv.csv" na pasta do programa, isso pode 
ser feito manualmente ou automaticamente através do própio programa escolhendo a opção 5, com isso você poderá escolher qualquer uma das outras opções sem
que o programa exiba um erro. As opções e suas funções são:

* **1. Exibir os dados da tabela csv:** Exibe na tela a tabela csv("dbcsv.csv") e seus registros formatados adequadamente.

* **2. Deletar registro:** Solicita ao usuário o nome da chave(coluna) onde está o item que ele quer usar como palavra-chave para definir o registro a ser deletado e 
após isso o nome do item contido no registro que ele quer deletar, se esse item existir nessa chave em algum dos registros da tabela csv, o programa deletará 
o primeiro registro do arquivo csv("dbcsv.csv") que atenda a essas condições e imprimirá na tela o registro deletado, se não encontrar nada ele simplesmente 
imprimirá na tela que "nenhum registro foi encontrado".

* **3. Adicionar registro:** Solicita ao usuário um nome(esse nome não pode conter vírgulas e nem aspas) para cada chave do registro de acordo com 
as chaves da tabela csv, depois disso o novo registro é salvo no arquivo csv("dbcsv.csv").

* **4. Buscar registro:** Solicita que seja inserido o nome da chave(coluna) onde está o item que será utilizado como palavra-chave para a busca do registro ou dos 
registros, depois o nome do item contido no(s) registro(s) a ser pesquisado, se esse item existir nessa chave em algum dos registros da 
tabela csv, o programa exibirá na tela todos os registros do arquivo csv("dbcsv.csv") que atendam a essas condições de busca, se não encotrar nada 
ele simplesmente imprimirá na tela que "nenhum registro foi encontrado".

* **5. Gerar arquivo csv:** Pede ao usuário para digitar os nomes das chaves(colunas) da tabela csv e cria o arquivo csv com o nome "dbcsv.csv" na pasta do programa. Os nomes das chaves não podem conter vírgulas e nem aspas.

Por fim para utilizar a tabela csv gerada e editada pelo programa no excel, basta abrir o excel, ir na aba dados, clicar em obter dados externos -> De texto,
escolher o arquivo csv, depois de escolher o arquivo se abrirá uma nova janela, nela mude a origem do arquivo para "1252: Europeu Ocidental (Windows)", clique
em avançar, agora nessa etapa escolha como delimitador a vírgula e avance para o próximo passo, depois clique em concluir, outra janela se abrirá e nela basta
escolher a célula onde quer importar a tabela csv e clicar em OK, pronto os dados do arquivo csv foram importados para o excel.

