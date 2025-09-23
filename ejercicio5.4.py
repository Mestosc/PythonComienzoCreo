from random import randint as rint

limite = 10

numero_secreto = rint(1, limite)

hechos = 0
intentos = 4

def pedir_numero(prompt: str) -> int | None:  # Al no poder importarse desde 2.5 lo hago así
    """
    La funcion pedira un numero y lo convertira a entero automaticamente
    Args:
        prompt: El prompt que se usara para pedir el numero
    Returns:
        El numero siendo un entero
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError as e:
            print(f"Introduce un valor valido, fallo: {e}")
            continue

def obtener_numero_mayor_menor(num_random: int, num_input: int) -> str:
    """
    Obtener la representacion textual(en palabras) de si es mayor o menor
    Args:
        num_random: El numero aleatorio que quiero adivinar
        num_input: El numero que proporcionas de input
    Returns:
        Mayor si el numero(num_input) es mayor que num_random, si num_input es menor que num_random devuelve menor
    """
    if num_input > num_random:
        return "mayor"
    else:
        return "menor"


while hechos < intentos:
    num = pedir_numero("Introduzca numero a adivinar: ")
    if num == numero_secreto:
        print("Enorabuena has ganado")
        break
    elif num > limite or num < 1:
        print("El numero que ha introducido esta fuera de rango")
    elif num != numero_secreto:
        print(f"El numero {num} es {obtener_numero_mayor_menor(numero_secreto, num)}")
        hechos += 1

if hechos == intentos:
    print(f"Lo siento has perdido, el numero era {numero_secreto}")