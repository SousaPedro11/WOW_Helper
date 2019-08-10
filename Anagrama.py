import itertools

import Utilitario as Util


def ana(word, tam, filtro=None):
    print("Anagramas:")
    cont = 0
    lista = list()
    if not filtro:
        filtro = None
    if filtro is None:
        verif = True
    anagramas = sorted(set(["".join(perm) for perm in itertools.permutations(word, tam)]))
    for x in range(len(anagramas)):
        if filtro is not None:
            palavra = filtrar(anagramas[x], filtro)
            if len(palavra.strip()) > 0:
                lista.append(palavra)
                cont = cont + 1
                print(str(cont) + "\t " + palavra)
        else:
            lista.append(anagramas[x])
            cont = cont + 1
            print(str(cont) + "\t " + anagramas[x])
    return lista


# def filtrar(palavra, regra, pos=None, letra=None):
def filtrar(palavra, regra):
    if regra is not None:
        letra, pos = tuple(x for x in regra.split(","))
        pos = int(pos)
        if palavra[pos - 1] == letra:
            return palavra
        else:
            return ""


def comparar(lista, dicionario):
    cont = 0
    print("\nPalavras no Dicionário:")
    for x in lista:
        if x in dicionario:
            cont += 1
            print(str(cont) + '\t' + x)


def resolver(nome_arquivo_dicionario):
    Util.clear()
    print("WOW Helper - Gera Anagramas e mostra quais são palavras válidas")
    resposta = True
    outra = False
    word = input("Digite uma palavra: ")
    while resposta or outra:
        if outra:
            Util.clear()
            word = input("Digite uma palavra: ")
        tam = input("Informe o tamanho do anagrama: ")
        filtro = (input("Informe a letra e posição: "))
        Util.clear()
        print("Palavra inserida: %s" % word.lower())
        print("Tamanho do anagrama: %s" % str(tam))
        print("Filtro inserido: %s" % str(filtro))
        comparar(Util.ler_dicionario(nome_arquivo_dicionario), ana(word, int(tam), filtro))
        usuario = input("Você deseja resolver outro problema com a palavra %s? (S/n): " % word.upper())
        # while (usuario is not 's' or usuario is not 'n') and (usuario is not 'S' or usuario is not 'N'):
        #     print("Informe corretamente as opções")
        #     usuario = input("Você deseja resolver outro problema com a palavra %s? (S/n)" % word.upper())

        if usuario is 'N' or usuario is 'n':
            ent_outra = input("deseja fazer para outra palavra?(s/N): ")
            if ent_outra is 's' or ent_outra is 'S':
                outra = True
            else:
                outra = False
                resposta = False

