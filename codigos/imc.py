import tkinter as tk
from tkinter import PhotoImage, messagebox

def button_clickud():
    # Muestra una ventana emergente con un mensaje cuando se presiona el botón
    messagebox.showinfo("notificacion", "el boton fue presionado")

# Crear la ventana principal
root = tk.Tk()
root.title("boton con imagen")  # Establece el título de la ventana principal

# Cargar la imagen para el botón
butimag = PhotoImage(file="IMC.png")

# Crear un botón con la imagen cargada y la función de clic definida
imagbut = tk.Button(root, image=butimag, command=button_clickud, borderwidth=4)
# El botón tiene un borde de 4 píxeles y ejecuta `button_clickud` cuando se hace clic

# Mostrar el botón en la ventana, con un relleno vertical de 20 píxeles
imagbut.pack(pady=20)

# Ejecutar el bucle principal de la ventana
root.mainloop()
