import networkx as nx
import random

def generar_mapa(num_regiones, num_colores):
    # Validar argumentos
    if not (16 <= num_regiones <= 30 and 3 <= num_colores <= 30):
        raise ValueError("La cantidad de regiones debe estar entre 16 y 30, y la cantidad de colores entre 3 y 30.")

    G = nx.Graph()

    colores = ["#{:06x}".format(random.randint(0, 0xFFFFFF)) for _ in range(num_colores)]

    for i in range(num_regiones):
        color = colores[i % num_colores]
        G.add_node(i, color=color)

    for i in range(num_regiones):
        conexiones_posibles = [j for j in range(num_regiones) if j != i and not G.has_edge(i, j)]
        conexiones_seleccionadas = random.sample(conexiones_posibles, min(2, len(conexiones_posibles)))
        for j in conexiones_seleccionadas:
            G.add_edge(i, j)

    return G, colores
