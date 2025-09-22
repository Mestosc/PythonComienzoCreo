contrasena_secreta = "bienvenido123#"


def pedir_contrasena_secreta(contrasena_secreta):
    intentos = 5
    hechos = 0
    while hechos<=intentos:
        contrasena = input("Introduzca la contraseña:")
        if contrasena_secreta == contrasena:
            print("Enorabuena lo has conseguido")
            return True
        elif hechos == intentos:
            print("Se han acabado los intentos")
            return False
        else:
            hechos += 1
            print(f"Has fallado: Quedan {intentos-hechos} intentos")
    return None


pedir_contrasena_secreta(contrasena_secreta)