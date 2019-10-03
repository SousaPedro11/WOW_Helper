# WOW_Helper
Gera anagramas a partir de uma palavra ou letras informadas e verifica os anagramas válidos segundo o dicionário (wordlist) palavras.txt

## Objetivos

+ Reconhecer uma palavra ou conjunto de letras como entrada.
+ Gerar lista de anagramas.
+ Filtrar anagramas gerados por tamanho.
    
     **Ex:**
        
        Entrada: medico
        Filtro de tamanho: 4
        Possiveis resultados: medo, cedo, come, comi, meio, mico , etc...

+ Filtrar anagramas gerados por letra em determinada posição (implementado 
apenas para 1 letra, por enquanto).

     **Ex:**
     
        Entrada: medico
        Filtro de tamanho: 4
        Filtro de letra e posição: e,3
        Possiveis resultados: coei, coem, doei, doem, icem, idem, moei.
        
+ Comparar os anagramas gerados com uma wordlist (palavras.txt) editável<sup>1</sup>.

## Utilização
### 1. Programa Principal
#### 1.1. Execução
    
Para executar as funções do programa com a Wordlist padrão,
basta executar o arquivo [Main.py](./Main.py).
 
Caso deseje executar com Wordlist personalizada, basta
abrir o arquivo [Main.py](./Main.py) e alterar a linha
```nome_Dicionario = "palavras.txt"``` para 
 ```nome_Dicionario = "caminho_wordlist"``` e depois executá-lo.
 
O programa executará as tarefas de acordo com as entradas
e depois perguntará:
```
Você deseja resolver outro problema com a palavra "palavra_fornecida_na_entrada"? (S/n):
```
*O programa entenderá que não apenas se for respondido **n** ou **N**, 
caso contrário assumirá uma resposta positiva.*

Se a reposta for positiva, o programa será reiniciado com a mesma 
palavra inserida na execução anterior. Apenas os filtros deverão ser inseridos.

Se a resposta da primeira pergunta for negativa haverá a seguinte pergunta:
```
Deseja resolver com outra palavra? (s/N)
```
*O programa assumirá resposta positiva apenas se for digitado **s** ou **S**, caso contrário a resposta será negativa 
e a execução encerrará. Caso a resposta seja positiva o programa executará pedindo todas as entradas.*
#### 1.2. Entrada
    
Assim que inicia a execução, as entradas são solicitadas na seguinte ordem:
##### 1.2.1. Palavra

É solicitado uma palavra ou um conjunto de letras (Ex: medico ou omidec).
##### 1.2.2. Filtro de tamanho

É solicitado um número inteiro que representa o
 tamanho dos anagramas a serem gerados. Ele deve ser 
 menor ou igual ao tamanho da palavra de entrada.
##### 1.2.3. Filtro letra/posição

É solicitada a letra e a posicao dela nos 
anagramas gerados no formato *letra,posição*. 
Este filtro é facultativo, e caso não seja inserido, 
os anagramas serão gerados apenas com o filtro de tamanho.

#### 1.3. Saída

A saída irá mostrar a palavra inserida, os filtros e em seguida o 
resultado da seguinte forma:

```
Anagramas:

1   anagrama 1

2   anagrama 2

.       .

.       .

.       .

n   anagrama n


Palavras no Dicionario

1   palavra 1

2   palavra 2

.       .

.       .

.       .

n   palavra n
```

### 2. Gerador de Wordlist
#### 2.1. Execução
Basta executar o programa [joinDitc.py](./joinDict.py) para gerar a WordList [palavras.txt](./palavras.txt).

#### 2.2. Entrada
A entrada para esse programa são os arquivos existentes na pasta [dicionarios_originais](dicionarios_originais).

##### 2.2.1. Para aumentar a WordList
Caso deseje adicionar novas palavras à WordList, basta criar um arquivo .txt contendo as novas palavras na
pasta [dicionarios_originais](dicionarios_originais).

##### 2.1.2. Para diminuir a WordList
Basta apagar as ocorrências das palavras a serem excluídas dos arquivos presentes na
pasta [dicionarios_originais](dicionarios_originais) e gerar novamente a WordList [palavras.txt](./palavras.txt).

#### 2.3. Saída
O programa [joinDitc.py](./joinDict.py) tem como retorno a criação da WordList no arquivo [palavras.txt](./palavras.txt) a partir da manipulação dos arquivos
existentes na pasta [dicionarios_originais](dicionarios_originais).

<hr />
<p>
<small>1. Pode ser aumentada ou diminuida a 
partir de um programa embutido.
</p>

