# WOW_Helper
Gera anagramas a partir de uma palavra ou letras informadas e verifica os anagramas válidos segundo o dicionário (wordlist) palavras.txt

## Objetivos

+ Reconhecer uma palavra ou conjunto de letras como entrada.
+ Gerar lista de anagramas.
+ Filtrar anagramas gerados por tamanho.
    
        **EXEMPLO**
        Entrada: medico
        Filtro de tamanho: 4
        Possiveis resultados: medo, cedo, come, comi, meio, mico , etc...

+ Filtrar anagramas gerados por letra em determinada posição (implementado 
apenas para 1 letra, por enquanto).

        **EXEMPLO**
        Entrada: medico
        Filtro de tamanho: 4
        Filtro de letra e posição: e,3
        Possiveis resultados: coei, coem, doei, doem, icem, idem, moei.
        
+ Compara os anagramas gerados com uma wordlist (palavras.txt) editável[^1].

[^1]: Pode ser aumentada ou diminuida a 
partir de um programa embutido.

##