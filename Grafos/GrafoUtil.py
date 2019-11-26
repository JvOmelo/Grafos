def buscaDFS(grafo, vertice, verticesVisitados, subgrafo, pai):

    if vertice not in verticesVisitados:

        if pai is not None:
            subgrafo.append((pai, vertice))
        pai = vertice

        verticesVisitados.append(vertice)


        for x in list(grafo[vertice]):
            if x != " ":
                buscaDFS(grafo, x, verticesVisitados, subgrafo, pai)
                

    return verticesVisitados, subgrafo
