"""
Operaciones
Descripción: Contiene las funciones básicas:
             sumar, restar, multiplicar y dividir.
"""

def sumar(a, b):
    """Suma dos números y devuelve el resultado."""
    return a + b


def restar(a, b):
    """Resta el segundo número al primero y devuelve el resultado."""
    return a - b


def multiplicar(a, b):
    """Multiplica dos números y devuelve el resultado."""
    return a * b


def dividir(a, b):
    """
    Divide a entre b y devuelve el resultado.

    Lanza:
        ValueError: si b es cero.
    """
    if b == 0:
        raise ValueError("Error: no se puede dividir entre cero.")
    return a / b

