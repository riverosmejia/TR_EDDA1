class Nodo:
    def __init__(self, id, nombre, latitud, longitud):
        self.id = id
        self.nombre = nombre
        self.latitud = latitud
        self.longitud = longitud

    def __str__(self):
        return f'[({self.id}) {self.nombre} | log:{self.longitud} lat:{self.latitud})\t]'

class Arista:
    def __init__(self, nodo_inicio, nodo_destino, peso):
        self.nodo_inicio = nodo_inicio
        self.nodo_destino = nodo_destino
        self.peso = peso

    def __str__(self):
        return f'ARISTA [{self.nodo_inicio} --> {self.nodo_destino}:: w:{self.peso}]'

class GrafoDirigido:
    def __init__(self):
        self.nodos = {}     # diccionario "HashTable"
        self.aristas = []   # lista

    def agregar_nodo(self, nodo):
        self.nodos[nodo.id] = nodo

    def agregar_arista(self, nodo_inicio, nodo_destino, peso):
        if nodo_inicio.id in self.nodos and nodo_destino.id in self.nodos:
            arista = Arista(nodo_inicio, nodo_destino, peso)
            self.aristas.append(arista)

    def mostrar_grafo(self):
        for arista in self.aristas:
            print(f"{arista}")

    def encontrar_camino(self, inicio_id, destino_id, camino_actual=None):
        if camino_actual is None:
            camino_actual = []  # lista
        inicio = self.nodos.get(inicio_id)
        destino = self.nodos.get(destino_id)
        if inicio is None or destino is None:
            print("\nADVERTENCIA: Nodo de inicio o destino no encontrado en el grafo.")
            return
        camino_actual = camino_actual + [inicio]
        if inicio == destino:
            self.mostrar_camino(camino_actual)
            return
        for arista in self.aristas:
            if arista.nodo_inicio == inicio and arista.nodo_destino not in camino_actual:
                self.encontrar_camino(arista.nodo_destino.id, destino_id, camino_actual[:])

    def mostrar_camino(self, camino):
        if camino:
            print("\nCAMINO ENCONTRADO:")
            costo_total = 0
            for i in range(len(camino) - 1):
                arista = self.buscar_arista(camino[i].id, camino[i + 1].id)
                print(f"{arista.nodo_inicio.nombre} -> {arista.nodo_destino.nombre} (Peso: {arista.peso})")
                costo_total += arista.peso
            print(f"Costo total del camino: [{costo_total} Km]\n")
            print('-'*20)

    def buscar_arista(self, inicio_id, destino_id):
        for arista in self.aristas:
            if arista.nodo_inicio.id == inicio_id and arista.nodo_destino.id == destino_id:
                return arista

# Ejemplo de uso
if __name__ == "__main__":
    grafo = GrafoDirigido()

    nodo_a = Nodo("A", "Punto A ", 40.728, 74.061)
    nodo_b = Nodo("B", "Lugar B ", 34.022, 18.237)
    nodo_c = Nodo("C", "Tienda C", 51.504, 10.128)
    nodo_d = Nodo("D", "Nodo D  ", 48.866, 22.322)

    grafo.agregar_nodo(nodo_a)
    grafo.agregar_nodo(nodo_b)
    grafo.agregar_nodo(nodo_c)
    grafo.agregar_nodo(nodo_d)

    grafo.agregar_arista(nodo_a, nodo_b, 5)
    grafo.agregar_arista(nodo_a, nodo_c, 4)
    grafo.agregar_arista(nodo_b, nodo_d, 3)
    grafo.agregar_arista(nodo_c, nodo_d, 7)

    grafo.mostrar_grafo()
    print("-"*20)
    print("\nBUSCAR CAMINOS: \n")

    estado = True
    while estado:
        inicio_id = input("ID de nodo de inicio: ")
        destino_id = input("ID de nodo de destino: ")

        grafo.encontrar_camino(inicio_id, destino_id)

        resp = input("¿Desea continuar? (S/N): ").strip().upper()
        if resp=='S':
            estado = True
        else:
            estado = False
