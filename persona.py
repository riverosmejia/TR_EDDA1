class persona:
    def __init__(self, telf, nombre):

        self.nombre = nombre
        self.telefono=telf

    def __str__(self):
        return f'persona: {self.nombre} -- teléfono: {self.telefono}'
