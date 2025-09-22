def obtener_numero_triangular(num: int):
    suma = 0
    for i in range(1,num+1):
        suma += i
    return suma

for i in range(1,6+1):
    print(f"{i}-{obtener_numero_triangular(i)}")

