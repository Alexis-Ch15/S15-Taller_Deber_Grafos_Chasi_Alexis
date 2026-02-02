from collections import deque
import heapq
grafo = {
    "A": ["B","C"],
    "B": ["A","D"],
    "C": ["A","D"],
    "D": ["B","C"]
}

print("### # RECORRIDO BSF POR AnCHURA ###")

def recorrido_anchura(grafo, nodoInicial):
    visitados=set()
    cola = deque([nodoInicial])

    while cola:
        nodo = cola.popleft()
        if nodo not in visitados:
            print(nodo, end=" ")
            visitados.add(nodo)
            cola.extend(grafo[nodo])

recorrido_anchura(grafo,"A")

print("\n### Recorrido DFS por profundidad ###")

def recorrido_profundidad(grafo,nodo, visitados=None):
    if visitados is None:
        visitados =set()
    print(nodo, end =" ")
    visitados.add(nodo)
    for vecino in grafo[nodo]:
        if vecino not in visitados:
            recorrido_profundidad(grafo,vecino,visitados)

recorrido_profundidad(grafo,"A")

grafo1={
    "A":["B"],
    "B":{"A"},
    "C":{"D"},
    "D":{"C"}
}
#Verificar si hay camino entre dos nodos:
def hay_camino(grafo, origen, destino):
    visitados = set()
    cola = deque([origen])

    while cola:
        nodo = cola.popleft()
        if nodo == destino:
            return True
        visitados.add(nodo)
        for vecino in grafo[nodo]:
            if vecino not in visitados and vecino not in cola:
                cola.append(vecino)
    
    return False

print("\nHay camino entre A y D?", hay_camino(grafo1, 'A', 'D'))  
print("Hay camino entre A y B?", hay_camino(grafo1, 'A', 'B'))  
print("Hay camino entre C y D?", hay_camino(grafo1, 'C', 'D'))  
print("Hay camino entre B y C?", hay_camino(grafo1, 'B', 'C'))  
#recorrer nodos no visitados

print("\nDesde B")
recorrido_profundidad(grafo,"B")
print("\nDesde C")
recorrido_profundidad(grafo,"C")
print("\nDesde D")
recorrido_profundidad(grafo,"D")
grafo2 = {
    'A': [('B', 1), ('C', 1)],
    'B': [('A', 1), ('D', 1)],
    'C': [('A', 1), ('D', 1)],
    'D': [('B', 1), ('C', 1)],
}


def dijkstra(grafo, origen):
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[origen] = 0
    heap = [(0, origen)]

    while heap:
        costo, nodo = heapq.heappop(heap)

        for vecino, peso in grafo[nodo]:
            nueva_dist = costo + peso
            if nueva_dist < distancias[vecino]:
                distancias[vecino] = nueva_dist
                heapq.heappush(heap, (nueva_dist, vecino))

    return distancias
print("\n",dijkstra(grafo2, "A"))

def topological_sort_dfs(grafo):
    visitados = set()
    orden = []

    def dfs(nodo):
        visitados.add(nodo)
        for vecino in grafo[nodo]:
            if vecino not in visitados:
                dfs(vecino)
        orden.append(nodo)

    for nodo in grafo:
        if nodo not in visitados:
            dfs(nodo)

    orden.reverse()
    return orden
print("\n",topological_sort_dfs(grafo))