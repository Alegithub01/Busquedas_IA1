# IA_Busquedas

Este proyecto implementa algoritmos de búsqueda de inteligencia artificial. Incluye una interfaz gráfica simple para ejecutar y visualizar los resultados de los algoritmos.

## Requisitos

Antes de ejecutar este proyecto, asegúrate de tener instaladas las siguientes herramientas y bibliotecas:

- Python 3.x: Puedes descargarlo desde [python.org](https://www.python.org/)
- Tkinter: La biblioteca de interfaz gráfica de Python, incluida en la mayoría de las distribuciones de Python.
- NetworkX: Biblioteca para la creación, manipulación y estudio de la estructura, dinámica y funciones de redes complejas.
- Matplotlib: Biblioteca para crear visualizaciones estáticas, animadas e interactivas en Python.

## Instalación

1. Clona este repositorio en tu máquina local:

git clone https://github.com/Alegithub01/Busquedas_IA1.git

2. Navega hasta el directorio del proyecto:

cd IA_Busquedas

3. Instala las dependencias utilizando pip:

pip install -r requeriments.txt


## Uso

Para ejecutar la interfaz gráfica, simplemente ejecuta el script `start.py`:

python start.py o python3 start.py

Esto abrirá la ventana principal de la aplicación desde donde podrás acceder a las diferentes funcionalidades.

## Estructura del Proyecto

- `start.py`: Script principal que inicia la interfaz gráfica.
- `image.png`: Archivo de imagen utilizado en la interfaz gráfica.
- `mapa.png`: Archivo de imagen utilizado en la interfaz gráfica.

### mapa
- `generar_mapa.py`: Contiene la función para generar un mapa aleatorio de nodos y aristas.
- `algoritmo_coloracion.py`: Implementación del algoritmo de coloración voraz.
- `visualizacion.py`: Funciones para visualizar el mapa inicial y final.
- `main.py`: Archivo principal para el inciso A.


### incisoB
-  `tresenraya_minimax.py`: Contiene la implementación del juego Tres en Raya utilizando el algoritmo Minimax para la búsqueda del mejor movimiento por parte de la inteligencia artificial.
