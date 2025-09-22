def generar_ficha_domino(num):
    separador = "\n\t"*(num-1)
    indicador = "*"*num
    ficha = ""
    for x in range(len(indicador)):
        ficha += indicador[y]
        for y in range(len(separador)):
            ficha += separador[y]
    print(ficha)


for i in range(1,7):
    generar_ficha_domino(i)