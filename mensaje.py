class relacion:
    def __init__(self, nodo_inicio, nodo_destino, peso,mensaje):
        self.nodo_inicio = nodo_inicio
        self.nodo_destino = nodo_destino
        self.peso = peso
        self.mensaje=[mensaje]


    def __str__(self):
        return f'ARISTA [{self.nodo_inicio} <--> {self.nodo_destino}:: peso de relacion: {self.peso}] mensajes: {self.mensaje}'

    def obtener_info(self):

        print(f'ARISTA [{self.nodo_inicio} <--> {self.nodo_destino}:: peso de relacion: {self.peso}]')

        for mensaje_ in self.mensaje:

            print(f'{mensaje_}')
