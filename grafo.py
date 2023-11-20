
from mensaje import relacion
from persona import persona

class GrafoDirigido:
    def __init__(self):

        self.personas = {}     
        self.relaciones = []   

    def agregar_nodo(self, nodo):
        self.personas[nodo] = nodo

    def agregar_arista(self, nodo_inicio, nodo_destino, peso):
        if nodo_inicio.telefono in self.personas and nodo_destino.telefono in self.personas:
            arista = persona(nodo_inicio, nodo_destino, peso)
            self.relaciones.append(arista)

    def mostrar_grafo(self):
        for arista in self.relaciones:
            print(f"{arista}")

    def encontrar_camino(self, inicio_id, destino_id, camino_actual=None):
        if camino_actual is None:
            camino_actual = []  # lista
        inicio = self.personas.get(inicio_id)
        destino = self.personas.get(destino_id)
        if inicio is None or destino is None:
            print("\nADVERTENCIA: Nodo de inicio o destino no encontrado en el grafo.")
            return
        camino_actual = camino_actual + [inicio]
        if inicio == destino:
            self.mostrar_camino(camino_actual)
            return
        for arista in self.relaciones:
            if arista.nodo_inicio == inicio and arista.nodo_destino not in camino_actual:
                self.encontrar_camino(arista.nodo_destino.id, destino_id, camino_actual[:])

    def buscar_arista(self, inicio_id, destino_id):
        for arista in self.relaciones:
            if arista.nodo_inicio.telefono == inicio_id and arista.nodo_destino.telefono == destino_id:
                return arista

    def encontrar_persona(self,persona):

        for per in self.personas:

            if per == persona:

                return True

        return False


