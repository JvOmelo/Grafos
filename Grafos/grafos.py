import sys
import Util

quantV = 0
Vertices = []
Arestas = []

quantV = int(input("Quantos vértices existem no grafo?: "))
for i in range(quantV):
    Vertices.append(input(f"Insira o {i+1} vértice: "))

#Digite apenas "S" para sim, ou "N" para não!!
for a in range(quantV):
    cont = 0
    cont += 1
    Arestas.append(input(f"{Vertices[a]} é adjacente a V{cont}?: ").upper())
    for v in range(quantV-1):
        Arestas.append(input(f"{Vertices[a]} é adjacente a V{cont+1}?: ").upper())
        cont += 1
matriz = []
for t in range(quantV):
    linha = []
    for n in range(quantV):
        linha.append(0)
    matriz.append(linha)

matrizV = []
contq = 0
contm = 0
for c in range(quantV):
    if Arestas[contq] == "S":
        matriz[c][0] = 1
    for g in range(quantV-1):
        contq+=1
        contm+=1
        if Arestas[contq] == "S":
            matriz[c][contm] = 1
    contq+=1
    contm = 0
print("MATRIZ DE ADJACENCIA:")
for t in range(quantV):
    print(matriz[t])

#Digite apenas "S" para sim, ou "N" para não!!
si = input(("Gostaria de utilizar a busca de articulação/Ordenação topologica/Fortemente conexo?\n").upper())
if si == "S" or si == "s":
    print("Insira um grafo não orientado e conexo para a busca de articulação!")
else:
    sys.exit()

while True:

    print("1 - AdicionarVertice \n2 - RemoverVertice \n3 - AdicionarAresta")
    print("4 - removerAresta \n5 - Ver o Grafo \n6 - Busca em profundidade")
    print("7 - Busca de articulações \n8 - Ordenação Topologica \n9 - Arvore Geradora")

    x = input("\nDigite o número que indica a operação que desejas.\n")

    if x == "1":
        Util.adicionarVertice()
    elif x == "2":
        Util.removerVertice()
    elif x == "3":
        Util.adicionarAresta()
    elif x == "4":
        Util.removerAresta()
    elif x == "5":
        print(Util.grafoDicio)
    elif x == "6":
        Util.busca_em_profundidade()
    elif x == "7":
        Util.Pontos_Articulacao()
    elif x == "8":
        Util.ordenacao_topologica()
    elif x == "9":
        Util.arvore_geradora()
    else:
        exit()
