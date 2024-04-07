import sys
from generar_mapa import generar_mapa
from algoritmo_coloracion import coloracion_voraz
from visualizacion import visualizar_mapa

def main(num_regiones, num_colores):
    # Generar el mapa
    G, colores = generar_mapa(num_regiones, num_colores)

    # Ejecutar el algoritmo de coloración
    costo_coloreo, coloreo = coloracion_voraz(G, colores)

    print("Costo del coloreo:", costo_coloreo)

    # Visualizar el mapa inicial y final
    visualizar_mapa(G, colores, coloreo)

if __name__ == "__main__":
    # Verificar si se proporcionaron los argumentos esperados
    if len(sys.argv) != 3:
        print("Uso: python main.py [num_regiones] [num_colores]")
        sys.exit(1)

    # Obtener los argumentos de la línea de comandos
    num_regiones = int(sys.argv[1])
    num_colores = int(sys.argv[2])

    # Llamar a la función main con los argumentos proporcionados
    main(num_regiones, num_colores)
