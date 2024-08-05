import tkinter as tk  #modulo para crear ventanas
from tkinter import PhotoImage, messagebox, Toplevel # se usa para mostrar una ventana
import tkinter.font as tkfont #creación y gestión de fuentes personalizadas en widgets
import csv #Permite manejar archivos CSV fácilmente

class IMCCalculator:
    def __init__(self, root):
        # Inicializa la calculadora de IMC y configura la interfaz gráfica
        self.root = root
        self.root.title("Calculadora de IMC")
        
        # Configura la imagen de fondo para la ventana principal
        self.configurar_fondo("ejemplo.png")
        
        # Configuración de la fuente y propiedades del texto
        font = ('Arial', 20)  # Fuente Arial, tamaño 20
        
        # Configura etiquetas para los campos de entrada con fuente Arial
        self.labnom = tk.Label(root, text="Nombre:", font=font, fg='green')
        self.labnom.grid(row=0, column=0, padx=10, pady=10, sticky=tk.E)
        
        self.labedad = tk.Label(root, text="Edad (años):", font=font, fg='green')
        self.labedad.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)
        
        self.labpeso = tk.Label(root, text="Peso (kg):", font=font, fg='green')
        self.labpeso.grid(row=2, column=0, padx=10, pady=10, sticky=tk.E)
        
        self.labalt = tk.Label(root, text="Altura (m):", font=font, fg='green')
        self.labalt.grid(row=3, column=0, padx=10, pady=10, sticky=tk.E)
        
        self.labsexo = tk.Label(root, text="Sexo:", font=font, fg='green')
        self.labsexo.grid(row=4, column=0, padx=10, pady=10, sticky=tk.E)
        
        # Configura la orientación de las etiquetas hacia la derecha
        for label in (self.labnom, self.labedad, self.labpeso, self.labalt, self.labsexo):
            label.config(justify=tk.RIGHT)  # Orientación hacia la derecha

        # Configura las entradas de texto con la fuente Arial
        self.entnomb = tk.Entry(root, font=font)
        self.entnomb.grid(row=0, column=1, padx=10, pady=10)
        
        self.entedad = tk.Entry(root, font=font)
        self.entedad.grid(row=1, column=1, padx=10, pady=10)
        
        self.entpeso = tk.Entry(root, font=font)
        self.entpeso.grid(row=2, column=1, padx=10, pady=10)
        
        self.entalt = tk.Entry(root, font=font)
        self.entalt.grid(row=3, column=1, padx=10, pady=10)

        # Configura los botones de radio para seleccionar el sexo
        self.radvar = tk.StringVar()
        self.radvar.set("Hombre")
        self.radhombre = tk.Radiobutton(root, text="Hombre", variable=self.radvar, value="Hombre", font=font, fg='green')
        self.radhombre.grid(row=4, column=1, padx=10, pady=5, sticky=tk.W)
        self.radmujer = tk.Radiobutton(root, text="Mujer", variable=self.radvar, value="Mujer", font=font, fg='green')
        self.radmujer.grid(row=4, column=1, padx=10, pady=5, sticky=tk.E)

        # Configura los botones para calcular el IMC y guardar los datos en CSV
        self.btncal = tk.Button(root, text="Calcular IMC", command=self.calcular_imc, cursor="hand2", font=font)
        self.btncal.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky=tk.N+tk.S+tk.E+tk.W)

        self.btnguar = tk.Button(root, text="Guardar en CSV", command=self.guardar_en_csv, cursor="hand2", font=font)
        self.btnguar.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky=tk.N+tk.S+tk.E+tk.W)

    def configurar_fondo(self, imagen_path):
        # Configura la imagen de fondo para la ventana principal
        fondo = PhotoImage(file=imagen_path)
        fonlabel = tk.Label(self.root, image=fondo)
        fonlabel.place(x=0, y=0, relwidth=1, relheight=1)
        fonlabel.image = fondo  # Mantiene la referencia para evitar que Python elimine la imagen

    def calcular_imc(self):
        # Calcula el IMC (Índice de Masa Corporal) y muestra el resultado
        try:
            # Obtiene los valores introducidos por el usuario
            peso = float(self.entpeso.get())
            altura = float(self.entalt.get())
            edad = int(self.entedad.get())
            nombre = self.entnomb.get()
            sexo = self.radvar.get()

            # Verifica que la altura sea mayor que cero
            if altura <= 0:
                messagebox.showerror("Error", "La altura debe ser mayor que cero.")
                return

            # Calcula el IMC con los factores de corrección basados en el sexo y la edad
            ks = 1.0 if sexo == "Hombre" else 1.1
            ka = 1 + 0.01 * (edad - 25)
            imc = (peso / (altura ** 2)) * ks * ka

            # Muestra el IMC calculado en un mensaje emergente
            messagebox.showinfo("IMC Calculado", f"El IMC calculado es: {imc:.2f}")

            # Muestra los resultados en una ventana emergente
            restexto = (
                f"Nombre: {nombre}\n"
                f"Edad: {edad}\n"
                f"Peso: {peso} kg\n"
                f"Altura: {altura} m\n"
                f"Sexo: {sexo}\n"
                f"IMC: {imc:.2f}"
            )
            messagebox.showinfo("Resultado del IMC", restexto)

        except ValueError:
            # Muestra un mensaje de error si los valores introducidos no son válidos
            messagebox.showerror("Error", "Por favor, introduce valores numéricos válidos.")

    def guardar_en_csv(self):
        # Guarda los datos introducidos en un archivo CSV
        try:
            # Obtiene los valores introducidos por el usuario
            peso = float(self.entpeso.get())
            altura = float(self.entalt.get())
            edad = int(self.entedad.get())
            nombre = self.entnomb.get()
            sexo = self.radvar.get()

            # Verifica que la altura sea mayor que cero
            if altura <= 0:
                messagebox.showerror("Error", "La altura debe ser mayor que cero.")
                return

            # Calcula el IMC con los factores de corrección basados en el sexo y la edad
            ks = 1.0 if sexo == "Hombre" else 1.1
            ka = 1 + 0.01 * (edad - 25)
            imc = (peso / (altura ** 2)) * ks * ka

            # Guarda los datos en un archivo CSV con el nombre del usuario
            nombre_archivo = f"{nombre}.csv"
            with open(nombre_archivo, mode='w', newline='') as file:
                writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                writer.writerow(['Nombre', 'Edad', 'Peso (kg)', 'Altura (m)', 'Sexo', 'IMC'])
                writer.writerow([nombre, edad, peso, altura, sexo, imc])

            # Muestra un mensaje de éxito al guardar el archivo
            messagebox.showinfo("Guardado exitoso", f"Datos guardados en {nombre_archivo}")

        except ValueError:
            # Muestra un mensaje de error si los valores introducidos no son válidos
            messagebox.showerror("Error", "Por favor, introduce valores numéricos válidos.")

def button_clickud():
    # Crea la ventana principal y configura la interfaz gráfica
    root = tk.Tk()
    root.title("Botón con IMC")
    
    # Configura el tamaño de la ventana principal
    root.geometry("1100x640")  # Tamaño arbitrario

    # Carga y configura la imagen de fondo
    backimage = tk.PhotoImage(file="ejemplo.png")
    backlabel = tk.Label(root, image=backimage)
    backlabel.place(relwidth=1, relheight=1)
    
    # Carga la imagen para el botón
    butima = PhotoImage(file="boton.png")

    # Crea el botón con la imagen y la función de clic para abrir la calculadora IMC
    imabutton = tk.Button(root, image=butima, command=abrir_calculadora_imc, borderwidth=4, cursor="hand2")
    imabutton.pack(pady=100, padx=100)  # Centra el botón en la ventana

    # Ejecuta el bucle principal de la ventana
    root.mainloop()

def abrir_calculadora_imc():
    # Crea una ventana emergente para la calculadora IMC
    root = tk.Toplevel()  # Usa Toplevel para abrir una nueva ventana sin cerrar la principal
    app = IMCCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    button_clickud()
