import re

# char codes: https://unicode-table.com/en/#basic-latin
accent_map = {
    u'\u00c0': u'A',
    u'\u00c1': u'A',
    u'\u00c2': u'A',
    u'\u00c3': u'A',
    u'\u00c4': u'A',
    u'\u00c5': u'A',
    u'\u00c6': u'A',
    u'\u00c8': u'E',
    u'\u00c9': u'E',
    u'\u00ca': u'E',
    u'\u00cb': u'E',
    u'\u00cc': u'I',
    u'\u00cd': u'I',
    u'\u00ce': u'I',
    u'\u00cf': u'I',
    u'\u00d0': u'D',
    u'\u00d1': u'N',
    u'\u00d2': u'O',
    u'\u00d3': u'O',
    u'\u00d4': u'O',
    u'\u00d5': u'O',
    u'\u00d6': u'O',
    u'\u00d7': u'x',
    u'\u00d8': u'0',
    u'\u00d9': u'U',
    u'\u00da': u'U',
    u'\u00db': u'U',
    u'\u00dc': u'U',
    u'\u00dd': u'Y',
    u'\u00df': u'B',
    u'\u00e0': u'a',
    u'\u00e1': u'a',
    u'\u00e2': u'a',
    u'\u00e3': u'a',
    u'\u00e4': u'a',
    u'\u00e5': u'a',
    u'\u00e6': u'a',
    u'\u00e8': u'e',
    u'\u00e9': u'e',
    u'\u00ea': u'e',
    u'\u00eb': u'e',
    u'\u00ec': u'i',
    u'\u00ed': u'i',
    u'\u00ee': u'i',
    u'\u00ef': u'i',
    u'\u00f1': u'n',
    u'\u00f2': u'o',
    u'\u00f3': u'o',
    u'\u00f4': u'o',
    u'\u00f5': u'o',
    u'\u00f6': u'o',
    u'\u00f8': u'0',
    u'\u00f9': u'u',
    u'\u00fa': u'u',
    u'\u00fb': u'u',
    u'\u00fc': u'u'
}


# u'\u00c7': u'C',u'\u00e7': u'c',


def accent_remove(m):
    letra = m.group(0)
    if letra != "ç" and letra != "Ç":
        return accent_map[m.group(0)]
    else:
        return letra


def remove_acento(palavra_velha):
    palavra_nova = re.sub(u'([\u00C0-\u00FC])', accent_remove, palavra_velha.encode().decode('utf-8'))
    return palavra_nova


def acento_lista(lista):
    lista_sem = list()
    for x in lista:
        novox = remove_acento(str(x))  # print(x)
        lista_sem.append(remove_barra(novox))
    return lista_sem


def remove_barra(palavra):
    x = palavra.split("/")
    palavra = x[0]
    return palavra


def ler_dicionario(nome_do_dicionario):
    lista_palavras_dicionario = [line.rstrip('\n') for line in open(nome_do_dicionario, encoding='utf8')]
    lista_palavras_dicionario = acento_lista(lista_palavras_dicionario)
    return lista_palavras_dicionario
