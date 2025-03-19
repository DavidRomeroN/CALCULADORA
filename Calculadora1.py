import tkinter as tk
from tkinter import messagebox

def calcular(operacion):
    try:
        num1 = float(entry1.get())  # Obtener el primer número
        num2 = float(entry2.get())  # Obtener el segundo número

        if operacion == "+":
            resultado = num1 + num2
        elif operacion == "-":
            resultado = num1 - num2
        elif operacion == "*":
            resultado = num1 * num2
        elif operacion == "/":
            if num2 == 0:
                messagebox.showerror("Error", "No se puede dividir entre 0")
                return
            resultado = num1 / num2

        label_resultado.config(text=f"Resultado: {resultado}")

    except ValueError:
        messagebox.showerror("Error", "Ingrese valores numéricos válidos")

# Crear ventana
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("300x250")

# Entradas de números
entry1 = tk.Entry(ventana)
entry1.pack(pady=5)

entry2 = tk.Entry(ventana)
entry2.pack(pady=5)

# Botones de operaciones
tk.Button(ventana, text="+", command=lambda: calcular("+")).pack(pady=2)
tk.Button(ventana, text="-", command=lambda: calcular("-")).pack(pady=2)
tk.Button(ventana, text="*", command=lambda: calcular("*")).pack(pady=2)
tk.Button(ventana, text="/", command=lambda: calcular("/")).pack(pady=2)

# Etiqueta de resultado
label_resultado = tk.Label(ventana, text="Resultado: ")
label_resultado.pack(pady=10)

# Ejecutar la ventana
ventana.mainloop()
