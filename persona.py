class persona:
    def __init__(self, nombre, telf):

        self.nombre = nombre
        self.telefono=telf

    def __str__ (self):

        return f'per:{self.nombre} -- tel:{self.telefono}'
