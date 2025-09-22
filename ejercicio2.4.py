def convertir_fahr_to_celsius(grados: int) -> float:
    """
    Converitr de fahr a Celsisus
    :param grados: Los grados Fahrenheit
    :return: los grados en celsius
    """
    return ((grados -32) * (5/9)).__round__(2)
print("Fahr\tCelsius")
for i in range(0,121):
    print(f"{i}ºF\t{convertir_fahr_to_celsius(i)}ºC")