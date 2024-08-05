import tkinter as tk
from tkinter import messagebox, PhotoImage
import csv

class IMCCalculator:
    def __init__(self, root):
        # Inicializa la ventana principal y configura la interfaz de usuario
        self.root = root
        self.root.title("Calculadora de IMC")

        # Crear y ubicar etiquetas y entradas para nombre, edad, peso, altura, y sexo
        self.labnom = tk.Label(root, text="Nombre:")
        self.labnom.grid(row=0, column=0, padx=10, pady=10)
        self.entnomb = tk.Entry(root)
        self.entnomb.grid(row=0, column=1, padx=10, pady=10)

        self.labedad = tk.Label(root, text="Edad (años):")
        self.labedad.grid(row=1, column=0, padx=10, pady=10)
        self.entedad = tk.Entry(root)
        self.entedad.grid(row=1, column=1, padx=10, pady=10)

        self.labpeso = tk.Label(root, text="Peso (kg):")
        self.labpeso.grid(row=2, column=0, padx=10, pady=10)
        self.entpeso = tk.Entry(root)
        self.entpeso.grid(row=2, column=1, padx=10, pady=10)

        self.labalt = tk.Label(root, text="Altura (m):")
        self.labalt.grid(row=3, column=0, padx=10, pady=10)
        self.entalt = tk.Entry(root)
        self.entalt.grid(row=3, column=1, padx=10, pady=10)

        self.labsexo = tk.Label(root, text="Sexo:")
        self.labexo.grid(row=4, column=0, padx=10, pady=10)
        self.radvar = tk.StringVar()
        self.radvar.set("Hombre")
        self.radhom = tk.Radiobutton(root, text="Hombre", variable=self.radvar, value="Hombre")
        self.radhom.grid(row=4, column=1, padx=10, pady=5, sticky=tk.W)
        self.radmujer = tk.Radiobutton(root, text="Mujer", variable=self.radvar, value="Mujer")
        self.radmujer.grid(row=4, column=1, padx=10, pady=5, sticky=tk.E)

        # Botón para calcular el IMC
        self.btncalc = tk.Button(root, text="Calcular IMC", command=self.calcular_imc)
        self.btncalc.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        # Botón para guardar los datos en un archivo CSV
        self.btnguar = tk.Button(root, text="Guardar en CSV", command=self.guardar_en_csv)
        self.btnguar.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    def calcular_imc(self):
        try:
            # Obtener los valores de las entradas y convertirlos a los tipos adecuados
            peso = float(self.entry_peso.get())
            altura = float(self.entry_altura.get())
            edad = int(self.entry_edad.get())
            nombre = self.entry_nombre.get()
            sexo = self.radio_var.get()

            # Validar que la altura sea mayor que cero
            if altura <= 0:
                messagebox.showerror("Error", "La altura debe ser mayor que cero.")
                return

            # Calcular el IMC
            ks = 1.0 if sexo == "Hombre" else 1.1
            ka = 1 + 0.01 * (edad - 25)
            imc = (peso / (altura ** 2)) * ks * ka

            # Mostrar el IMC en un mensaje emergente
            messagebox.showinfo("IMC Calculado", f"El IMC calculado es: {imc:.2f}")

            # Mostrar los resultados en una segunda ventana
            self.mostrar_segunda_ventana(nombre, edad, peso, altura, sexo, imc)

        except ValueError:
            # Mostrar un mensaje de error si hay un valor no válido
            messagebox.showerror("Error", "Por favor, introduce valores numéricos válidos.")

    def guardar_en_csv(self):
        try:
            # Obtener los valores de las entradas y convertirlos a los tipos adecuados
            peso = float(self.entry_peso.get())
            altura = float(self.entry_altura.get())
            edad = int(self.entry_edad.get())
            nombre = self.entry_nombre.get()
            sexo = self.radio_var.get()

            # Validar que la altura sea mayor que cero
            if altura <= 0:
                messagebox.showerror("Error", "La altura debe ser mayor que cero.")
                return

            # Calcular el IMC
            ks = 1.0 if sexo == "Hombre" else 1.1
            ka = 1 + 0.01 * (edad - 25)
            imc = (peso / (altura ** 2)) * ks * ka

            # Guardar los datos en un archivo CSV
            nomarc = f"{nombre}.csv"
            with open(nomarc, mode='w', newline='') as file:
                writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                writer.writerow(['Nombre', 'Edad', 'Peso (kg)', 'Altura (m)', 'Sexo', 'IMC'])
                writer.writerow([nombre, edad, peso, altura, sexo, imc])

            # Mostrar un mensaje de éxito
            messagebox.showinfo("Guardado exitoso", f"Datos guardados en {nomarc}")

        except ValueError:
            # Mostrar un mensaje de error si hay un valor no válido
            messagebox.showerror("Error", "Por favor, introduce valores numéricos válidos.")

    def mostrar_segunda_ventana(self, nombre, edad, peso, altura, sexo, imc):
        # Crear una nueva ventana para mostrar los resultados
        segven = tk.Toplevel(self.root)
        segven.title("Resultado del IMC")

        # Crear y ubicar una etiqueta con los resultados en la nueva ventana
        label_resultado = tk.Label(segven, text=f"Nombre: {nombre}\nEdad: {edad}\nPeso: {peso} kg\nAltura: {altura} m\nSexo: {sexo}\nIMC: {imc:.2f}")
        label_resultado.pack(padx=20, pady=20)

# Ejecutar la aplicación si el archivo se ejecuta directamente
if __name__ == "__main__":
    root = tk.Tk()
    app = IMCCalculator(root)
    root.mainloop()
