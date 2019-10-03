import codecs
from os import listdir

import Utilitario as Util

nome_wordlist = 'palavras.txt'


def ler_dicionario(nome_do_dicionario):
    nome_do_dicionario = "dicionarios_originais/" + nome_do_dicionario
    lista_palavras_dicionario = [line.rstrip('\n') for line in open(nome_do_dicionario, encoding='utf8')]
    lista_palavras_dicionario = Util.acento_lista(lista_palavras_dicionario)
    return lista_palavras_dicionario


def join_dict():
    setlist = set()
    caminhopasta = "dicionarios_originais"
    for x in listdir(caminhopasta):
        for _ in ler_dicionario(x):
            if _ not in setlist:
                setlist.add(_)
        print("'" + x + "'", "adicionado à WordList", nome_wordlist.replace(".txt", ""))
    return sorted(setlist)


def salvar():
    lista = join_dict()
    f = codecs.open(nome_wordlist, 'w', 'utf8')
    [f.write(x + '\n') for x in lista]
    print("\nO arquivo " + nome_wordlist, "foi criado com êxito.")


salvar()
