import tkinter as tk
from tkinter import messagebox
from maquinaTuring import process_string  

def process_input():
    input_string = entry.get()

    if not set(input_string).issubset({"0", "1"}):
        messagebox.showerror("Error", "Por favor, ingresa solo 0s y 1s.")
        return

    result = process_string(input_string)


    result_label.config(text="Resultado: " + result.split("_")[0])


root = tk.Tk()
root.title("Simulador de Máquina de Turing")
root.minsize(400, 400)

container = tk.Frame(root)
container.pack(expand=True, fill='both')

label = tk.Label(container, text="Ingresa una cadena de 0s y 1s:", font=("Arial", 16))
label.pack(pady=30)

entry = tk.Entry(container, width=40, font=("Arial", 14))
entry.pack(pady=5)


button = tk.Button(container, text="Procesar", command=process_input, font=("Arial", 14))
button.pack(pady=10)

result_label = tk.Label(container, text="Resultado: ", font=("Arial", 16))
result_label.pack(pady=20)


root.mainloop()
