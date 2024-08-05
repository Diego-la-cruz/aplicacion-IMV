import tkinter as tk
from tkinter import PhotoImage, messagebox

def button_clickud():
    # Función que se ejecuta cuando el botón es presionado
    # Muestra un mensaje emergente con una notificación
    messagebox.showinfo("notificacion", "el boton fue presionado")

# Crear la ventana principal
root = tk.Tk()
root.title("boton con imagen")

# Cargar la imagen para el botón
# Se asume que "IMC.png" es una imagen en el directorio actual
butimag = PhotoImage(file="IMC.png")

# Crear un botón que usa la imagen cargada y asignar la función a ejecutar al hacer clic
# borderwidth=4 define el ancho del borde del botón
imagbut = tk.Button(root, image=butimag, command=button_clickud, borderwidth=4)

# Colocar el botón en la ventana principal con un relleno vertical de 20 píxeles
imagbut.pack(pady=20)

# Iniciar el bucle principal de la interfaz gráfica
root.mainloop()
