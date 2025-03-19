def calculadora():
    while True:
        try:
            num1 = float(input("Ingrese el primer número: "))
            operador = input("Ingrese la operación (+, -, *, /): ")
            num2 = float(input("Ingrese el segundo número: "))

            if operador == "+":
                resultado = num1 + num2
            elif operador == "-":
                resultado = num1 - num2
            elif operador == "*":
                resultado = num1 * num2
            elif operador == "/":
                if num2 == 0:
                    resultado = "ERROR: División por cero"
                else:
                    resultado = num1 / num2
            else:
                resultado = "ERROR: Operación inválida"

            # Salida de datos
            print(f"Resultado: {resultado}")

        except ValueError:
            print("ERROR: Entrada inválida. Ingrese números válidos.")

        # Preguntar si se desea realizar otra operación
        nueva_op = input("¿Desea realizar otra operación? (s/n): ").strip().lower()
        if nueva_op != 's':
            print("Calculadora finalizada.")
            break

# Ejecutar la calculadora
calculadora()
