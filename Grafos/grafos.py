Vertices = []
Arestas = []
quantV = 0

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
