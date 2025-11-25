import Operaciones

def leer_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada inválida. Debes escribir un número.\n")

def leer_operacion():
    opciones = {
        "1": ("suma", "Suma(1)"),
        "2": ("resta", "Resta(2)"),
        "3": ("multiplicacion", "Multiplicación(3)"),
        "4": ("division", "División(4)")
    }

    while True:
        print("\nElige la operación:")
        print("  Suma(1)")
        print("  Resta(2)")
        print("  Multiplicación(3)")
        print("  División(4)")
        entrada = input("Escribe el número o el nombre de la operación: ").strip().lower()

        if entrada in opciones:
            return opciones[entrada]

        for _, (nombre, etiqueta) in opciones.items():
            if entrada == nombre:
                return nombre, etiqueta

        print("Operación no válida. Intenta de nuevo.\n")

def main():
    print("=== CALCULADORA ===\n")

    while True:
        a = leer_numero("Ingresa el primer número: ")
        b = leer_numero("Ingresa el segundo número: ")
        operacion, etiqueta = leer_operacion()

        print(f"\nOperación seleccionada: {etiqueta}")

        try:
            if operacion == "suma":
                resultado = Operaciones.sumar(a, b)
                simbolo = "+"
            elif operacion == "resta":
                resultado = Operaciones.restar(a, b)
                simbolo = "-"
            elif operacion == "multiplicacion":
                resultado = Operaciones.multiplicar(a, b)
                simbolo = "*"
            elif operacion == "division":
                resultado = Operaciones.dividir(a, b)
                simbolo = "/"

            print(f"Resultado: {a} {simbolo} {b} = {resultado}\n")
        except ValueError as e:
            print(f"\n{e}\n")

        continuar = input("¿Quieres realizar otra operación? (s/n): ").strip().lower()
        if continuar != "s":
            print("\nGracias.")
            break

if __name__ == "__main__":
    main()
