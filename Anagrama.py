import itertools


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
