def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")

    return a / b


def mostrar_resultados():
    print("================================")
    print("      CALCULADORA EN PYTHON")
    print("================================")

    numero1 = 20
    numero2 = 5

    print(f"Suma: {numero1} + {numero2} = {sumar(numero1, numero2)}")
    print(f"Resta: {numero1} - {numero2} = {restar(numero1, numero2)}")
    print(
        f"Multiplicacion: {numero1} x {numero2} = "
        f"{multiplicar(numero1, numero2)}"
    )
    print(
        f"Division: {numero1} / {numero2} = "
        f"{dividir(numero1, numero2)}"
    )

    print("================================")
    print("Programa ejecutado correctamente")
    print("================================")


if __name__ == "__main__":
    mostrar_resultados()