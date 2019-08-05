import Utilitario as Util
import codecs


def join_set(setlist, lista):
    print('s antes:', len(setlist))
    temp = [setlist.add(x) for x in lista if x not in setlist]
    print('temp:', len(temp))
    print('s depois', len(setlist))


def salvar(lista):
    # with open('teste.txt', 'w') as f:
    #     f.writelines(lista)
    f = codecs.open('../palavras.txt', 'w', 'utf8')
    # f.writelines(list(lista))
    [f.write(x+'\n') for x in lista]


portuguese = Util.ler_dicionario('Portuguese (Brazilian).txt')
wordlist_ao = Util.ler_dicionario('wordlist-ao-latest.txt')
wordlist_big = Util.ler_dicionario('wordlist-big-latest.txt')
wordlist_preao = Util.ler_dicionario('wordlist-preao-latest.txt')

big_set = set()
print("\nadd portuguese")
join_set(big_set, portuguese)
print("\nadd preao")
join_set(big_set, wordlist_preao)
print("\nadd ao")
join_set(big_set, wordlist_ao)
print("\nadd big")
join_set(big_set, wordlist_big)

salvar(list(sorted(big_set)))
