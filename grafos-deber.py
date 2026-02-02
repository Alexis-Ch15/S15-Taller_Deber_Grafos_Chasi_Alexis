from collections import deque
grafo = {
    "D": ["B", "C", "H"],
    "B": ["D"],
    "C": ["D", "R"],
    "H": ["D", "A", "T"],
    "R": ["C"],
    "A": ["H"],
    "T": ["H"]
}

def BFS(grafo, nodo_inicial):
    visitados = set()
    cola = deque([nodo_inicial])
    visitados.add(nodo_inicial)

    while cola:
        nodo = cola.popleft()
        print(nodo, end=" ")

        for vecino in grafo[nodo]:
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append(vecino)

print("Recorrido BFS")
BFS(grafo,"D")

def DFS(grafo,nodo,visitados=None):
    if visitados is None:
        visitados=set()
    print(nodo, end=" ")
    visitados.add(nodo)
    for vecino in grafo[nodo]:
        if vecino not in visitados:
            DFS(grafo, vecino,visitados)
print("\nRecorrido DFS")
DFS(grafo,"D")