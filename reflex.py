#aqui irá el codigo que une a todo el grafo más reflex, por ahora solo irá el caso de uso.

from mensaje import relacion
from persona import persona
from grafo import GrafoDirigido

# Ejemplo de uso
if __name__ == "__main__":

    grafo = GrafoDirigido()

    persona1=persona('miguel',1038)
    persona2=persona('joseph',1039)
    persona3=persona('victor',1040)

    grafo.agregar_nodo(persona1)
    grafo.agregar_nodo(persona2)
    grafo.agregar_nodo(persona3)

    print(grafo.personas)




