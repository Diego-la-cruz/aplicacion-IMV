import tkinter as tk
from tkinter import messagebox, PhotoImage
import csv

class IMCCalculator(tk.Toplevel):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Calculadora de IMC")
        self.configure(bg="#f0f0f0")  # Color de fondo

        # Estilo para las etiquetas
        label_style = {
            "bg": "#f0f0f0",  # Color de fondo
            "fg": "#333333",  # Color de texto
            "font": ("Helvetica", 12),  # Fuente y tamaño
            "padx": 10,
            "pady": 10
        }

        # Estilo para las entradas
        entry_style = {
            "bg": "#ffffff",  # Color de fondo
            "fg": "#333333",  # Color de texto
            "font": ("Helvetica", 12),  # Fuente y tamaño
            "highlightbackground": "#cccccc",  # Color de borde al seleccionar
            "highlightcolor": "#333333",  # Color de borde al seleccionar
            "highlightthickness": 1,
            "relief": "solid",
            "width": 15
        }

        # Configuración de la ventana
        self.geometry("400x300")  # Tamaño inicial de la ventana
        self.resizable(False, False)  # Evitar que se redimensione

        # Etiquetas y entradas
        self.label_nombre = tk.Label(self, text="Nombre:", **label_style)
        self.label_nombre.grid(row=0, column=0)
        self.entry_nombre = tk.Entry(self, **entry_style)
        self.entry_nombre.grid(row=0, column=1)

        self.label_edad = tk.Label(self, text="Edad (años):", **label_style)
        self.label_edad.grid(row=1, column=0)
        self.entry_edad = tk.Entry(self, **entry_style)
        self.entry_edad.grid(row=1, column=1)

        self.label_peso = tk.Label(self, text="Peso (kg):", **label_style)
        self.label_peso.grid(row=2, column=0)
        self.entry_peso = tk.Entry(self, **entry_style)
        self.entry_peso.grid(row=2, column=1)

        self.label_altura = tk.Label(self, text="Altura (m):", **label_style)
        self.label_altura.grid(row=3, column=0)
        self.entry_altura = tk.Entry(self, **entry_style)
        self.entry_altura.grid(row=3, column=1)

        self.label_sexo = tk.Label(self, text="Sexo:", **label_style)
        self.label_sexo.grid(row=4, column=0)
        self.radio_var = tk.StringVar()
        self.radio_var.set("Hombre")
        self.radio_hombre = tk.Radiobutton(self, text="Hombre", variable=self.radio_var, value="Hombre", **label_style)
        self.radio_hombre.grid(row=4, column=1, sticky=tk.W)
        self.radio_mujer = tk.Radiobutton(self, text="Mujer", variable=self.radio_var, value="Mujer", **label_style)
        self.radio_mujer.grid(row=4, column=1, sticky=tk.E)

        # Botones
        button_style = {
            "bg": "#4CAF50",  # Color de fondo
            "fg": "white",  # Color de texto
            "font": ("Helvetica", 12),  # Fuente y tamaño
            "padx": 10,
            "pady": 5,
            "borderwidth": 2,
            "relief": "groove",
            "width": 15
        }

        self.btn_calcular = tk.Button(self, text="Calcular IMC", command=self.calcular_imc, **button_style)
        self.btn_calcular.grid(row=5, column=0, columnspan=2, pady=10)

        self.btn_guardar = tk.Button(self, text="Guardar en CSV", command=self.guardar_en_csv, **button_style)
        self.btn_guardar.grid(row=6, column=0, columnspan=2, pady=10)

    def calcular_imc(self):
        try:
            peso = float(self.entry_peso.get())
            altura = float(self.entry_altura.get())
            edad = int(self.entry_edad.get())
            nombre = self.entry_nombre.get()
            sexo = self.radio_var.get()

            if altura <= 0:
                messagebox.showerror("Error", "La altura debe ser mayor que cero.")
                return

            ks = 1.0 if sexo == "Hombre" else 1.1
            ka = 1 + 0.01 * (edad - 25)
            imc = (peso / (altura ** 2)) * ks * ka

            messagebox.showinfo("IMC Calculado", f"El IMC calculado es: {imc:.2f}")

        except ValueError:
            messagebox.showerror("Error", "Por favor, introduce valores numéricos válidos.")

    def guardar_en_csv(self):
        try:
            peso = float(self.entry_peso.get())
            altura = float(self.entry_altura.get())
            edad = int(self.entry_edad.get())
            nombre = self.entry_nombre.get()
            sexo = self.radio_var.get()

            if altura <= 0:
                messagebox.showerror("Error", "La altura debe ser mayor que cero.")
                return

            ks = 1.0 if sexo == "Hombre" else 1.1
            ka = 1 + 0.01 * (edad - 25)
            imc = (peso / (altura ** 2)) * ks * ka

            nombre_archivo = f"{nombre}.csv"
            with open(nombre_archivo, mode='w', newline='') as file:
                writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                writer.writerow(['Nombre', 'Edad', 'Peso (kg)', 'Altura (m)', 'Sexo', 'IMC'])
                writer.writerow([nombre, edad, peso, altura, sexo, imc])

            messagebox.showinfo("Guardado exitoso", f"Datos guardados en {nombre_archivo}")

        except ValueError:
            messagebox.showerror("Error", "Por favor, introduce valores numéricos válidos.")

def button_clickud():
    second_window = IMCCalculator(root)
    root.wait_window(second_window)  # Esperar hasta que se cierre la segunda ventana

root = tk.Tk()
root.title("Botón con imagen")

# Cargar la imagen para el fondo
background_image = tk.PhotoImage(file="ejemplo.png")

# Configurar un Label con la imagen de fondo
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Cargar la imagen para el botón
button_imagen = PhotoImage(file="IMC.png")

# Crear el botón con la imagen y la función de clic, y cambiar el cursor a una mano
imagen_button = tk.Button(root, image=button_imagen, command=button_clickud, bd=0, highlightthickness=0, cursor="hand2")
imagen_button.pack(pady=20)

root.mainloop()