import tkinter as tk
from tkinter import messagebox

def obtener_numeros():
    """Obtiene y convierte los valores ingresados a float. Muestra un error si no son válidos."""
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        return num1, num2
    except ValueError:
        messagebox.showerror("Error", "Ingrese valores numéricos válidos")
        return None, None

def sumar():
    num1, num2 = obtener_numeros()
    if num1 is not None:
        label_resultado.config(text=f"Resultado: {num1 + num2}")

def restar():
    num1, num2 = obtener_numeros()
    if num1 is not None:
        label_resultado.config(text=f"Resultado: {num1 - num2}")

def multiplicar():
    num1, num2 = obtener_numeros()
    if num1 is not None:
        label_resultado.config(text=f"Resultado: {num1 * num2}")

def dividir():
    num1, num2 = obtener_numeros()
    if num1 is not None:
        if num2 == 0:
            messagebox.showerror("Error", "No se puede dividir entre 0")
        else:
            label_resultado.config(text=f"Resultado: {num1 / num2}")

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
tk.Button(ventana, text="+", command=sumar).pack(pady=2)
tk.Button(ventana, text="-", command=restar).pack(pady=2)
tk.Button(ventana, text="*", command=multiplicar).pack(pady=2)
tk.Button(ventana, text="/", command=dividir).pack(pady=2)

# Etiqueta de resultado
label_resultado = tk.Label(ventana, text="Resultado: ")
label_resultado.pack(pady=10)

# Ejecutar la ventana
ventana.mainloop()
