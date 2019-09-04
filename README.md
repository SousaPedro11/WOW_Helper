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
        
+ Compara os anagramas gerados com uma wordlist (palavras.txt) editável<sup>1</sup>.

## Utilização
1. Programa Principal
    1. Execução
    
        Para executar as funções do programa com a Wordlist padrão,
         basta executar o arquivo [Main.py](./Main.py).
         Caso deseje executar com Wordlist personalizada, basta
         abrir o arquivo [Main.py](./Main.py) e alterar a linha
         ```nome_Dicionario = "palavras.txt"``` para 
         ```nome_Dicionario = "caminho_wordlist"```
    2. Entrada
    3. Filtros
    4. Saída

2. Gerador de Wordlist

<hr />
<p>
<small>1. Pode ser aumentada ou diminuida a 
partir de um programa embutido.
</p>

