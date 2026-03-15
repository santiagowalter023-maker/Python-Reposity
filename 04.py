import tkinter as tk
from tkinter import messagebox


# FUNCION PARA CALCULAR PRECIO
def calcular_precio(bochas):

    if bochas == 1:
        return 700

    if bochas == 2:
        return 1200

    if bochas == 3:
        return 1600


# FUNCION PARA MOSTRAR SABORES
def mostrar_sabores():
    frame_sabores.pack(pady=20)
    boton_final.pack(pady=20)
    boton_siguiente.pack_forget()


# FUNCION FINAL
def terminar():

    sabores = []

    if limon_var.get() == 1:
        sabores.append("Limon")

    if frutilla_var.get() == 1:
        sabores.append("Frutilla")

    if anana_var.get() == 1:
        sabores.append("Anana")

    if nranja_var.get() == 1:
        sabores.append("Naranja")

    if vainilla_var.get() == 1:
        sabores.append("Vainilla")

    if ddeleche_var.get() == 1:
        sabores.append("Dulce de leche")

    if tramntan_var.get() == 1:
        sabores.append("Tramontana")


    bochas = opcion_t.get()

    if bochas == 0:
        messagebox.showinfo("Error", "Elegí la cantidad de bochas")
        return


    if len(sabores) > bochas:
        messagebox.showinfo("Error", "Elegiste más sabores que bochas")
        return


    precio = calcular_precio(bochas)


    messagebox.showinfo(
        "Resumen del pedido",
        "Bochas: " + str(bochas) +
        "\nSabores: " + str(sabores) +
        "\nPrecio: $" + str(precio)
    )


ventana = tk.Tk()
ventana.title("Heladería Dulce Frío")
ventana.geometry("400x450")


# SECCION BOCHAS
opcion_t = tk.IntVar()

tk.Label(ventana, text="Elegir cantidad de bochas").pack()

tk.Radiobutton(ventana, text="1 Bocha", variable=opcion_t, value=1).pack()
tk.Radiobutton(ventana, text="2 Bochas", variable=opcion_t, value=2).pack()
tk.Radiobutton(ventana, text="3 Bochas", variable=opcion_t, value=3).pack()


boton_siguiente = tk.Button(
    ventana,
    text="Elegir Sabores",
    command=mostrar_sabores
)
boton_siguiente.pack(pady=10)


# SABORES
frame_sabores = tk.Frame(ventana)

limon_var = tk.IntVar()
frutilla_var = tk.IntVar()
anana_var = tk.IntVar()
nranja_var = tk.IntVar()
vainilla_var = tk.IntVar()
ddeleche_var = tk.IntVar()
tramntan_var = tk.IntVar()

tk.Checkbutton(frame_sabores, text="Limon", variable=limon_var).pack()
tk.Checkbutton(frame_sabores, text="Frutilla", variable=frutilla_var).pack()
tk.Checkbutton(frame_sabores, text="Anana", variable=anana_var).pack()
tk.Checkbutton(frame_sabores, text="Naranja", variable=nranja_var).pack()
tk.Checkbutton(frame_sabores, text="Vainilla", variable=vainilla_var).pack()
tk.Checkbutton(frame_sabores, text="Dulce de leche", variable=ddeleche_var).pack()
tk.Checkbutton(frame_sabores, text="Tramontana", variable=tramntan_var).pack()


boton_final = tk.Button(
    ventana,
    text="Confirmar Pedido",
    command=terminar
)


ventana.mainloop()