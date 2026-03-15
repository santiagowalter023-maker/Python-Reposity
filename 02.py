import tkinter as tk
from tkinter import messagebox

#FUNCION
def mostrar_sabores():
    frame_sabores.pack(pady=20)
    boton_final.pack(pady=20)
    boton_siguiente.pack_forget()

def terminar():

    tamanos = []
    sabores = []

    if limon_var.get() == 1:
        sabores.append("Limon")
        tamanos.append(limon_t.get())

    if frutilla_var.get() == 1:
        sabores.append("Frutilla")
        tamanos.append(frutilla_t.get())

    if anana_var.get() == 1:
        sabores.append("Anana")
        tamanos.append(anana_t.get())

    if nranja_var.get() == 1:
        sabores.append("Naranja")
        tamanos.append(nranja_t.get())

    if vainilla_var.get() == 1:
        sabores.append("Vainilla")
        tamanos.append(vainilla_t.get())

    if ddeleche_var.get() == 1:
        sabores.append("DulceDeLeche")
        tamanos.append(ddeleche_t.get())

    if tramntan_var.get() == 1:
        sabores.append("Tramontana")
        tamanos.append(tramntan_t.get())

    messagebox.showinfo("Heladería", "Sabores: " + str(sabores) + "\nTamaños: " + str(tamanos))
    ventana.destroy()


ventana = tk.Tk()
ventana.title("Menú Heladería")
ventana.geometry("500x500")
ventana.configure(bg="#88b9fa")

# VARIABLES DE TAMAÑO
limon_t = tk.IntVar()
frutilla_t = tk.IntVar()
anana_t = tk.IntVar()
nranja_t = tk.IntVar()
vainilla_t = tk.IntVar()
ddeleche_t = tk.IntVar()
tramntan_t = tk.IntVar()

lbl_paso1 = tk.Label(ventana, text="1. ELIGE SABORES Y TAMAÑO", font=("Arial", 12, "bold"),fg="#D02090", bg="#FFF0F5")
lbl_paso1.pack(pady=15)

# Botón para mostrar sabores
boton_siguiente = tk.Button(ventana, text="Elegir Sabores de la casa",command=mostrar_sabores, bg="#FFB6C1")
boton_siguiente.pack(pady=10)

# FRAME SABORES
frame_sabores = tk.Frame(ventana, bg="#FFFFFF")

tk.Label(frame_sabores, text="SABORES AL AGUA", fg="#008B8B", bg="#FFF0F5").grid(row=0, column=0)
tk.Label(frame_sabores, text="SABORES A LA CREMA", fg="#8B4513", bg="#FFF0F5").grid(row=0, column=1)

tk.Label(frame_sabores, text="1B").grid(row=0, column=2)
tk.Label(frame_sabores, text="2B").grid(row=0, column=3)
tk.Label(frame_sabores, text="1/4").grid(row=0, column=4)

# VARIABLES SABORES
limon_var = tk.IntVar()
frutilla_var = tk.IntVar()
anana_var = tk.IntVar()
nranja_var = tk.IntVar()
vainilla_var = tk.IntVar()
ddeleche_var = tk.IntVar()
tramntan_var = tk.IntVar()

# LIMON
tk.Checkbutton(frame_sabores, text="Limón", variable=limon_var).grid(row=1, column=0)
tk.Radiobutton(frame_sabores, variable=limon_t, value=1).grid(row=1, column=2)
tk.Radiobutton(frame_sabores, variable=limon_t, value=2).grid(row=1, column=3)
tk.Radiobutton(frame_sabores, variable=limon_t, value=3).grid(row=1, column=4)

# FRUTILLA
tk.Checkbutton(frame_sabores, text="Frutilla", variable=frutilla_var).grid(row=2, column=0)
tk.Radiobutton(frame_sabores, variable=frutilla_t, value=1).grid(row=2, column=2)
tk.Radiobutton(frame_sabores, variable=frutilla_t, value=2).grid(row=2, column=3)
tk.Radiobutton(frame_sabores, variable=frutilla_t, value=3).grid(row=2, column=4)

# ANANA
tk.Checkbutton(frame_sabores, text="Ananá", variable=anana_var).grid(row=3, column=0)
tk.Radiobutton(frame_sabores, variable=anana_t, value=1).grid(row=3, column=2)
tk.Radiobutton(frame_sabores, variable=anana_t, value=2).grid(row=3, column=3)
tk.Radiobutton(frame_sabores, variable=anana_t, value=3).grid(row=3, column=4)

# NARANJA
tk.Checkbutton(frame_sabores, text="Naranja", variable=nranja_var).grid(row=4, column=0)
tk.Radiobutton(frame_sabores, variable=nranja_t, value=1).grid(row=4, column=2)
tk.Radiobutton(frame_sabores, variable=nranja_t, value=2).grid(row=4, column=3)
tk.Radiobutton(frame_sabores, variable=nranja_t, value=3).grid(row=4, column=4)

# VAINILLA
tk.Checkbutton(frame_sabores, text="Vainilla", variable=vainilla_var).grid(row=2, column=1)
tk.Radiobutton(frame_sabores, variable=vainilla_t, value=1).grid(row=2, column=2)
tk.Radiobutton(frame_sabores, variable=vainilla_t, value=2).grid(row=2, column=3)
tk.Radiobutton(frame_sabores, variable=vainilla_t, value=3).grid(row=2, column=4)

# DULCE DE LECHE
tk.Checkbutton(frame_sabores, text="Dulce de Leche", variable=ddeleche_var).grid(row=3, column=1)
tk.Radiobutton(frame_sabores, variable=ddeleche_t, value=1).grid(row=3, column=2)
tk.Radiobutton(frame_sabores, variable=ddeleche_t, value=2).grid(row=3, column=3)
tk.Radiobutton(frame_sabores, variable=ddeleche_t, value=3).grid(row=3, column=4)

# TRAMONTANA
tk.Checkbutton(frame_sabores, text="Tramontana", variable=tramntan_var).grid(row=4, column=1)
tk.Radiobutton(frame_sabores, variable=tramntan_t, value=1).grid(row=4, column=2)
tk.Radiobutton(frame_sabores, variable=tramntan_t, value=2).grid(row=4, column=3)
tk.Radiobutton(frame_sabores, variable=tramntan_t, value=3).grid(row=4, column=4)

# BOTON FINAL
boton_final = tk.Button(ventana, text="CONFIRMAR PEDIDO", command=terminar,
                        bg="#32CD32", fg="white", font=("Arial", 11, "bold"))

ventana.mainloop()