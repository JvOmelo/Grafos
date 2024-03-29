from GrafoUtil import buscaDFS as dfs
import Busca_Articulacao
import sys
grafoDicio = dict()
contGraph = 0
listVerticeE = []
listV = []
def adicionarVertice():
    global grafoDicio
    #EVITE USAR "V" NA FRENTE DO NOME DO VERTICE!!
    vertice = input("\nInsira o nome do vértice. Deve ser um número de 0 a 9(Não use 'V' na frente do numero): ")
    grafoDicio[vertice] = ""

    return grafoDicio


def removerVertice():
    global grafoDicio

    verticeParaRemover = input("\nDigite o vértice que deseja remover: ")

    if verticeParaRemover not in grafoDicio:
        print("\nEsse vértice inexiste.")
        verticeParaRemover = input("\nDigite o vértice que deseja remover: ")

    grafoDicio.pop(verticeParaRemover, None)

    return grafoDicio

def adicionarAresta():
    global grafoDicio
    global contGraph
    global listVerticeE
    global listV
    contGraph += 1
    verticeE = input("\nPara qual vértice você deseja adicionar uma aresta?\n")

    while verticeE not in grafoDicio:
        print("Esse vértice não existe.")
        verticeE = input("\nPara qual vértice você deseja adicionar uma aresta?\n")

    v = input("\nDigite o vértice ao qual este vértice está ligado.\n")

    while v not in grafoDicio:
        print("\nEsse vértice inexiste.")
        v = input("\nDigite o vértice ao qual este vértice está ligado.\n")

    if v not in grafoDicio[verticeE]:
        grafoDicio[verticeE] = grafoDicio[verticeE] + str(v) + " "
        print(grafoDicio)
    else:
        print("\nEssa aresta já existe!")
    listVerticeE.append(verticeE)
    listV.append(v)

    return grafoDicio


def Pontos_Articulacao():
    global contGraph
    global listVerticeE
    global listV

    g = Busca_Articulacao.Graph(contGraph)
    for i in range(contGraph):
        g.addEdge(listVerticeE[i], listV[i])
    g.AP()


def ordenacao_topologica():

    global grafoDicio

    VOrdenacao = input("\nDigite o vértice com grau de entrada nulo para iniciar a busca da ordenação topologica.\n")

    while VOrdenacao not in grafoDicio:
        print("Esse vértice não existe.")
        VOrdenacao = input("\nDigite o vértice para iniciar a busca da ordenação topologica.\n")

    origemVisitado, origemSubgrafo = dfs(grafoDicio, VOrdenacao, [], [], None)
    print(origemVisitado, origemSubgrafo)
    lista = []
    for i in range(len(origemVisitado)):
        lista.append([origemVisitado[i]])
        grafoDicio.pop(origemVisitado[i], None)
    print(lista)
    return grafoDicio

def arvore_geradora():

    global grafoDicio
    arvore = []
    dfs = []
    dfs = dfs(grafoDicio, grafoDicio[0], [], [], None)
    while True:
        if dfs in grafoDicio:
            arvore.append(dfs)
    else:
        exit()
    return arvore

def removerAresta():

    global grafoDicio

    verticeE = input("\nDe qual vértice origem você gostaria de remover uma aresta?: ")
    while verticeE not in grafoDicio:
        print("Esse vértice não existe.")
        verticeE = input("\nDe qual vértice origem você gostaria de remover uma aresta?: ")
    listaDeArestasVerticeX = list(grafoDicio[verticeE])

    arestaE = input("\nDigite o vértice com qual o vértice digitado faz a aresta que desejas remover: ")
    while arestaE not in listaDeArestasVerticeX:
        print("A aresta inexiste.")
        arestaE = input("\nDigite o vértice com qual o vértice digitado faz a aresta que desejas remover: ")

    cont = 0
    while cont < len(listaDeArestasVerticeX):
        if listaDeArestasVerticeX[cont] == arestaE:
            del listaDeArestasVerticeX[cont]
            del listaDeArestasVerticeX[cont]
            break
        cont += 1

    grafoDicio[verticeE] = "".join(listaDeArestasVerticeX)

    return grafoDicio

def busca_em_profundidade():

    if grafoDicio:

        origem = input("\nDigite a origem (vértice pelo qual você deseja começar a busca até o final): ")

        while origem not in grafoDicio:

            print("\nEsse vértice não está no grafo!")
            origem = input("\nDigite a origem (vértice pelo qual você deseja começar a busca até o final): ")

        visitados, subgrafo = dfs(grafoDicio, origem, [], [], None)

        print("\nOrdem da busca: ", end="")
        print(*visitados, sep=", ", end=".\n")
        print("Subgrafo (pai, filho): ", end="")
        print(*subgrafo, sep=", ", end=".\n")

    else:
        print("\nO grafo está vazio!")

    return 0
