from random import randint as rint
def pedir_numero(prompt: str) -> int | None: # Al no poder importarse desde 2.5 lo hago así
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

limite = 10

numero_secreto = rint(1,limite)

hechos = 0
intentos = 4

def obtener_numero_mayor_menor(num_random,num_input):
    if num_input>num_random:
        return "mayor"
    else:
        return "menor"


while hechos<intentos:
    num = pedir_numero("Introduzca numero a adivinar: ")
    if num == numero_secreto:
        print("Enorabuena has ganado")
        break
    elif num>limite or num<1:
        print("El numero que ha introducido esta fuera de rango")
    elif num!=numero_secreto:
        print(f"El numero {num} es {obtener_numero_mayor_menor(numero_secreto, num)}")
        hechos += 1