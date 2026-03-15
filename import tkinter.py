<<<<<<< HEAD
import tkinter

ventana = tkinter.Tk()
ventana.geometry("400x300")

etiqueta = tkinter.Label(ventana,  text = "Heladeria el Walter",  bg= "green")
etiqueta.pack(fill = tkinter.X)

etiqueta2 = tkinter.Button(ventana,  text = "SALIR", bg= "red")
etiqueta2.pack(side = tkinter.BOTTOM)

def mensaje(grande):
    print("BElGRANO"+ grande)

botton = tkinter.Button(ventana, text = "¿Que helado quiere?", command = lambda: mensaje(" EL MAS GRANDE"))
botton.pack(side= tkinter.LEFT)

texto = tkinter.Entry(ventana, font= ("Times New Roman",12))
texto.pack(side= tkinter.RIGHT)

def textos():
    tex = texto.get()
    print(tex)

botton2 = tkinter.Button(ventana, text= "Presionar", command= textos)
botton2.pack()
#
#Usa escala grid
#botton3 = tkinter.Button(ventana, text= "Aguante Belgrano")
#botton3.grid(row=2)
#no se puede mezclar con el pack en una misma ventana
#


ventana.mainloop()

=======
import tkinter

ventana = tkinter.Tk()
ventana.geometry("400x300")

etiqueta = tkinter.Label(ventana,  text = "Heladeria el Walter",  bg= "green")
etiqueta.pack(fill = tkinter.X)

etiqueta2 = tkinter.Button(ventana,  text = "SALIR", bg= "red")
etiqueta2.pack(side = tkinter.BOTTOM)

def mensaje(grande):
    print("BElGRANO"+ grande)

botton = tkinter.Button(ventana, text = "¿Que helado quiere?", command = lambda: mensaje(" EL MAS GRANDE"))
botton.pack(side= tkinter.LEFT)

texto = tkinter.Entry(ventana, font= ("Times New Roman",12))
texto.pack(side= tkinter.RIGHT)

def textos():
    tex = texto.get()
    print(tex)

botton2 = tkinter.Button(ventana, text= "Presionar", command= textos)
botton2.pack()
#
#Usa escala grid
#botton3 = tkinter.Button(ventana, text= "Aguante Belgrano")
#botton3.grid(row=2)
#no se puede mezclar con el pack en una misma ventana
#


ventana.mainloop()

>>>>>>> 692ac206a8349129a2ce8251fb4df7c4a7055e2d
