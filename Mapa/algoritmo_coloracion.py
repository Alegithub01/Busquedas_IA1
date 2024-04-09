def coloracion_voraz(graph, colores):
    iteraciones = 0
    cambios = 0
    coloreo = {}
    
    nodos = graph.nodes()

    for nodo in nodos:
        colores_disponibles = set(colores)

        for vecino in graph.neighbors(nodo):
            if vecino in coloreo:
                colores_disponibles.discard(coloreo[vecino])

        if colores_disponibles:
            color = colores_disponibles.pop()
        else:
            color = colores[iteraciones % len(colores)]
            cambios += 1
        iteraciones += 1  
        coloreo[nodo] = color
    costo = iteraciones + cambios
    
    # Evaluar si la búsqueda es completa y óptima
    completo = "Sí" if len(coloreo) == len(nodos) else "No"
    optimo = "No" 

    # Calcular el costo temporal y espacial
    costo_temporal = iteraciones
    costo_espacial = iteraciones

    print("Búsqueda completa:", completo)
    print("Búsqueda óptima:", optimo)
    print("Costo temporal:", costo_temporal)
    print("Costo espacial:", costo_espacial)

    return costo, coloreo
