
from mensaje import relacion
from persona import persona

class Grafo:
    def __init__(self):

        self.personas = {}     
        self.relaciones = []   

    def agregar_nodo(self, nodo):
        #print(nodo)
        self.personas[nodo] = nodo

    def agregar_arista(self, nodo_inicio, nodo_destino,mensaje,fecha):

        arista_nueva = relacion(nodo_inicio, nodo_destino,1,[str(mensaje),str(fecha)])
        arista_existente = self.buscar_arista(nodo_destino, nodo_inicio)

        if arista_existente is None:
            #print(arista_nueva)
            self.relaciones.append(arista_nueva)
        else:
            #print(arista_existente)
            # Si ya existe una arista en la dirección opuesta, actualiza su peso
            arista_existente.peso = arista_existente.peso + 1
            arista_existente.mensaje.append([str(mensaje),str(fecha)])


    def mostrar_grafo(self):
        for arista in self.relaciones:
            print(f"{arista}")

    def mostrar_personas(self):
        cont1=0
        for personas in self.personas:
            cont1+=1
            print(f'{cont1}. {personas.nombre}')

    def mostrar_relaciones(self):
        for mensajes in self.relaciones:
            print(mensajes)

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

    def encontrar_persona(self,persona):

        for per in self.personas:

            if per.nombre == persona:

                return True

        return False

    def buscar_arista(self, inicio, destino):
        for arista in self.relaciones:
            if arista.nodo_inicio == inicio and arista.nodo_destino == destino:
                return arista
        return None
        
    def persona_con_mas_relacion(self, persona_tel):
        print(f"Buscando relaciones para el número de teléfono: {persona_tel}")
        # Buscar la instancia de persona correspondiente al número de teléfono
        persona_actual = None
        for persona_instancia in self.personas.values():
            if persona_instancia.telefono == persona_tel:
                persona_actual = persona_instancia
                break

        if persona_actual is None:
            print(f"La persona con el teléfono {persona_tel} no está en el grafo.")
            return

        print(persona_actual)

        # Obtener todas las relaciones que involucran a la persona actual
        relaciones_con_persona = []

        for relacion in self.relaciones:

            #print(f'{relacion.nodo_inicio} -- {relacion.nodo_destino}')

            if persona_actual.nombre == relacion.nodo_inicio or persona_actual.nombre == relacion.nodo_destino:

                relaciones_con_persona.append(relacion)

        if not relaciones_con_persona:
            print(f"La persona con el teléfono {persona_tel} no tiene relaciones, es más hermitaña que Riveros.")
            return

        # Encontrar la relación con el mayor peso
        max_relacion = max(relaciones_con_persona, key=lambda r: r.peso)

        # Determinar la otra persona en la relación
        if persona_actual.nombre==max_relacion.nodo_destino:
            other_person = max_relacion.nodo_inicio
        elif persona_actual.nombre==max_relacion.nodo_inicio:
            other_person=max_relacion.nodo_destino

        print(f"La persona con mayor relación con la persona {persona_actual.nombre} es {other_person} "
            f"con un peso de {max_relacion.peso}.")
        

