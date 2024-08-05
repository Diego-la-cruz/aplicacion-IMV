import tkinter as tk
from PIL import Image, ImageTk

def main():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("GUI con imagen de fondo y botón")

    # Cargar la imagen de fondo usando PIL (Python Imaging Library)
    image = Image.open("ejemplo.png")
    backimag = ImageTk.PhotoImage(image)

    # Obtener las dimensiones de la imagen para ajustar el tamaño del canvas
    img_width, img_height = image.size

    # Crear un canvas con el tamaño de la imagen para colocar la imagen de fondo
    canvas = tk.Canvas(root, width=img_width, height=img_height)
    canvas.pack(fill="both", expand=True)

    # Colocar la imagen de fondo en el canvas. La imagen se ancla en la esquina superior izquierda (nw).
    canvas.create_image(0, 0, image=backimag, anchor="nw")

    # Cargar la imagen para el botón
    butimag = Image.open("IMC.png")
    butphoto = ImageTk.PhotoImage(butimag)

    # Crear un botón con la imagen cargada. El botón no tiene borde y tiene un cursor de mano al pasar el ratón.
    button = tk.Button(root, image=butphoto, bd=0, cursor="hand2", command=lambda: print("Botón presionado"))
    button.image = butphoto  # Mantener una referencia a la imagen del botón para evitar que el recolector de basura la elimine

    # Colocar el botón en el canvas, centrado horizontalmente y a una altura de 350 píxeles desde la parte superior
    canvas.create_window(img_width // 2, 350, window=button)

    # Ejecutar el bucle principal de la ventana
    root.mainloop()

if __name__ == "__main__":
    main()

