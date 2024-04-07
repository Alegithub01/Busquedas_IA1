import tkinter as tk
from subprocess import Popen
from tkinter import messagebox
from PIL import Image, ImageTk

def salir():
    ventana.destroy()
    
def mostrar_mapa():
    ventana_mapa = tk.Toplevel()
    ventana_mapa.title("Inciso A")

    try:
        imagen_mapa = Image.open("mapa.png")
        imagen_mapa = ImageTk.PhotoImage(imagen_mapa)
        ventana_mapa.imagen_mapa = imagen_mapa 
    except FileNotFoundError:
        print("Error: No se pudo encontrar la imagen 'mapa.png'")
        return
    except Exception as e:
        print("Error al cargar la imagen:", e)
        return

    # Mostrar imagen
    label_imagen = tk.Label(ventana_mapa, image=imagen_mapa)
    label_imagen.pack()

    # Texto de descripción
    texto_descripcion = tk.Label(ventana_mapa, text="Este mapa está representado por nodos y aristas. Al presionar ejecutar, se generará un mapa aleatorio")
    texto_descripcion.pack()
    
    texto_descripcion = tk.Label(ventana_mapa, text="con nodos y aristas conectadas. Se mostrará el mapa inicial y el mapa una vez aplicada la metodología de búsqueda.")
    texto_descripcion.pack()

    # Función para validar la entrada como un número y dentro del rango especificado
    def validar_entrada(entrada, min_valor, max_valor):
        valor = entrada.get()
        if not valor.isdigit():
            messagebox.showerror("Error", "Ingrese un número entero.")
            return False
        valor = int(valor)
        if valor < min_valor or valor > max_valor:
            messagebox.showerror("Error", f"Ingrese un número entre {min_valor} y {max_valor}.")
            return False
        return True

    # Campos de entrada para la cantidad de regiones y colores
    frame_campos = tk.Frame(ventana_mapa)
    frame_campos.pack()

    label_regiones = tk.Label(frame_campos, text="Cantidad de regiones (16-30):")
    label_regiones.grid(row=0, column=0)
    entry_regiones = tk.Entry(frame_campos)
    entry_regiones.grid(row=0, column=1)

    label_colores = tk.Label(frame_campos, text="Cantidad de colores (3-30):")
    label_colores.grid(row=1, column=0)
    entry_colores = tk.Entry(frame_campos)
    entry_colores.grid(row=1, column=1)

    # Botón de ejecutar
    boton_ejecutar = tk.Button(ventana_mapa, text="Ejecutar", command=lambda: ejecutar_algoritmo_mapa(entry_regiones, entry_colores))
    boton_ejecutar.pack()

    # Botón de cerrar
    boton_cerrar = tk.Button(ventana_mapa, text="Cerrar", command=ventana_mapa.destroy)
    boton_cerrar.pack()
        
    def ejecutar_algoritmo_mapa(entry_regiones, entry_colores):
        # Validar entrada de regiones
        if not validar_entrada(entry_regiones, 16, 30):
            return
        num_regiones = int(entry_regiones.get())

        # Validar entrada de colores
        if not validar_entrada(entry_colores, 3, 30):
            return
        num_colores = int(entry_colores.get())

        # Ejecutar main.py con los argumentos proporcionados
        proceso = Popen(["python3", "incisoA/main.py", str(num_regiones), str(num_colores)])
        proceso.wait()


def mostrar_inciso_b():
    ventana_inciso_b = tk.Toplevel()
    ventana_inciso_b.title("Inciso B")
    # Aquí agregar la funcionalidad para el inciso B

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Metodologías de Búsqueda")

# Cargar imagen
imagen = Image.open("image.png")
imagen = ImageTk.PhotoImage(imagen)

# Mostrar imagen
label_imagen = tk.Label(ventana, image=imagen)
label_imagen.pack()

# Botones
boton_inciso_a = tk.Button(ventana, text="Inciso A", command=mostrar_mapa)
boton_inciso_a.pack()

boton_inciso_b = tk.Button(ventana, text="Inciso B", command=mostrar_inciso_b)
boton_inciso_b.pack()

boton_salir = tk.Button(ventana, text="Salir", command=salir)
boton_salir.pack()

# Centrar ventana en la pantalla
ancho_ventana = 800
alto_ventana = 600
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()
x = (ancho_pantalla - ancho_ventana) // 2
y = (alto_pantalla - alto_ventana) // 2
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

ventana.mainloop()
