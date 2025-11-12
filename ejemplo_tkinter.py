from tkinter import Button, Entry, Label, Tk

ventana = Tk()
ventana.title("Ventana principal")
ventana.geometry("640x480")
ventana.resizable(False, False)
ventana.configure(bg="white")

lbl_nombre = Label(ventana, text="Ingrese su nombre:", fg="blue")
lbl_nombre.pack(pady=25) # No olviden poner .pack() a todos los widgets

nombre = Entry(ventana, width=50)
nombre.pack(pady=0)

lbl_apellido = Label(ventana, text="Ingrese su apellido:", fg="blue")
lbl_apellido.pack(pady=25)

apellido = Entry(ventana, width=50)
apellido.pack(pady=0)

def saludar():
    _nombre = nombre.get()
    _apellido = apellido.get()
    resultante.config(text=f"Hola {_nombre} {_apellido}")

btn_saludar = Button(ventana, text="¡Saludar!", command=saludar) # Recuerden poner la funcion sin parentesis (deben definir antes la funcion)
btn_saludar.pack(pady=25)

resultante = Label(ventana, text="", font=("Arial",20,"bold"))
resultante.pack(pady=50)

ventana.mainloop() # Si o si el metodo mainloop() para renderizar la ventana principal