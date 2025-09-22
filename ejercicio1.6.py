def calcular_perimetro_area_rectangulo(base,altura):
    """
    Calcula el area y el perimetro de un rectangulo usando su base y altura
    :param base: La base del rectangulo
    :param altura: La altura del rectangulo
    :return: El area y el perimetro del rectangulo
    """
    area = base * altura
    perimetro = 2 * (base + altura)
    return area,perimetro
def calcular_area_permitero_circulo(radio: int):
    pass

print(calcular_perimetro_area_rectangulo(12,21))
