class relacion:
    def __init__(self, nodo_inicio, nodo_destino, peso):
        self.nodo_inicio = nodo_inicio
        self.nodo_destino = nodo_destino
        self.peso = peso

    def __str__(self):
        return f'ARISTA [{self.nodo_inicio} <--> {self.nodo_destino}:: peso de relacion:{self.peso}]'
