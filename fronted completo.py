from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from collections import Counter

# Función para calcular la frecuencia de los caracteres en un archivo
def calcular_frecuencia():
    # Pedir al usuario que seleccione un archivo
    archivo = filedialog.askopenfilename()  
    if archivo:
        # Leer el contenido del archivo y contar la frecuencia de cada carácter
        with open(archivo, 'r', encoding='utf-8') as f:  
            contenido = f.read()
            frecuencia = Counter(contenido)
            # Ordenar la lista de frecuencias en orden 
            lista_frecuencia = sorted(frecuencia.items(), key=lambda x: x[1], reverse=True)
            # Mostrar la lista de frecuencias en una nueva ventana
            mostrar_frecuencia(lista_frecuencia)

# Función para mostrar la lista de frecuencia de caracteres en una nueva ventana
def mostrar_frecuencia(lista_frecuencia):
    ventana_frecuencia = Toplevel(root)
    ventana_frecuencia.title("Lista de Frecuencia de Caracteres")

    # Crear una barra de desplazamiento
    txt_frecuencia = Text(ventana_frecuencia, wrap=NONE)
    scrollbar = Scrollbar(ventana_frecuencia, orient=VERTICAL, command=txt_frecuencia.yview)
    txt_frecuencia.config(yscrollcommand=scrollbar.set)

    # Mostrar la lista de frecuencia en el Textbox
    for item in lista_frecuencia:
        txt_frecuencia.insert(END, f"{item[0]} : {item[1]}\n")
    
    # Empacar el Textbox y la barra de desplazamiento
    txt_frecuencia.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.pack(side=RIGHT, fill=Y)

# Función para comprimir un archivo
def comprimir():
    print("Comprimir")

# Función para descomprimir un archivo
def descomprimir():
    print("Descomprimir")

# Configuración de la interfaz de usuario
root = Tk()
root.title("ACT 07 - Entrega 1 Huffman")
root.geometry("400x430")

frm = ttk.Frame(root, padding=10)
frm.grid()

# Etiqueta de bienvenida
ttk.Label(frm, text="Bienvenido a tu programa de confianza para comprimir archivos").grid(column=1, row=0)

# Botones, despues del command se cambia de nombre si tienes otro nombre en la función
ttk.Button(frm, text="Examinar", command=calcular_frecuencia).grid(column=1, row=1)
ttk.Button(frm, text="Comprimir", command=comprimir).grid(column=1, row=2)
ttk.Button(frm, text="Descomprimir", command=descomprimir).grid(column=1, row=3)
ttk.Button(frm, text="Salir", command=root.destroy).grid(column=1, row=4)

root.mainloop()
