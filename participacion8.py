from tkinter import *
from tkinter import ttk
from tkinter import filedialog

def buscar():
    #archivo = Tk.filedialog.Directory()
    
    #archivo = buscar()
   # print(archivo)

    archivo = filedialog.askdirectory()
    archivo = buscar()
    print(archivo)

    #archivo = filedialog.askopenfilenames(mode='r')
    #archivo = buscar()
    #print(archivo)

def comprimir():



    print()



root = Tk()
root.title("participacion 08")
root.geometry("400x430")

frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Bienvenido a tu programa de confianza para comprimir archivos").grid(column=1, row=0)
ttk.Button(frm, text="Buscar archivo", command=buscar).grid(column=1, row=1)
ttk.Button(frm, text="Comprimir", command=comprimir).grid(column=1, row=2)
ttk.Button(frm, text="Quitar", command=root.destroy).grid(column=1, row=3)

root.mainloop()