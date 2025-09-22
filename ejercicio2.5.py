def pedir_numero(prompt: str) -> int | None:
    """
    La funcion pedira un numero y lo convertira a entero automaticamente
    Args:
        prompt El prompt que se usara para pedir el numero
    Returns:
        El numero siendo un entero
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError as e:
            print(f"Introduce un valor valido, fallo: {e}")
            continue


num1 = pedir_numero("Introduzca primer numero:")
num2 = pedir_numero("Introduzca segundo numero:")

for i in range(num1, num2 + 1):
    if i % 2 == 0:
        print(i)
