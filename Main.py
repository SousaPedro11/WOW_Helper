import Anagrama
import Utilitario as Util

nomeDicionario = "palavras.txt"

word = input("Digite uma palavra: ")
tam = input("Informe o tamanho do anagrama: ")
filtro = (input("Informe a letra e posição: "))

Anagrama.comparar(Util.ler_dicionario(nomeDicionario), Anagrama.ana(word, int(tam), filtro))
