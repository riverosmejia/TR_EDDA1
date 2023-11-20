#Ejemplo basico de grafos

class Data:
    def __init__(self, valor):
        self.valor = valor

class Grafo:
    def __init__(self):
        self.nodos = {} #para simplificar la busqueda

    def agregar_nodo(self, nodo): #Los nodos son diferentes
        if nodo not in self.nodos:
            self.nodos[nodo] = []

    def valencia(self, nodo):
        if nodo in self.nodos:
            return len(self.nodos[nodo])
        return None

    def agregar_arista(self, nodoOrigen, nodoDestino):
        if nodoOrigen in self.nodos and nodoDestino in self.nodos:
            self.nodos[nodoOrigen].append(nodoDestino)
            #self.nodos[nodoDestino].append(nodoOrigen) #es para grafos no dirigidos

    def __str__(self):
        respuesta = ""
        for nodo,adyacencias in self.nodos.items():
            respuesta += str(nodo.valor) + "-->" + ", ".join(str(ady.valor) for ady in adyacencias) + " Valencia: "+ str(self.valencia(nodo)) + "\n"
            
        return respuesta

if __name__ == "__main__":
    nodo1 = Data('A')
    nodo2 = Data('B')
    nodo3 = Data('C')
    nodo4 = Data('D')

    grafo = Grafo()
    grafo.agregar_nodo(nodo1)
    grafo.agregar_nodo(nodo2)
    grafo.agregar_nodo(nodo3)
    grafo.agregar_nodo(nodo4)
    grafo.agregar_arista(nodo1, nodo2)
    grafo.agregar_arista(nodo1, nodo3)
    grafo.agregar_arista(nodo2, nodo4)
    grafo.agregar_arista(nodo3, nodo4)
    print(grafo)
