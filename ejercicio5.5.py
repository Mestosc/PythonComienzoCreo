def maximo_comun_divisor(num1,num2):
    resto = num1 % num2
    if resto == 0:
        return num2
    return maximo_comun_divisor(num2,resto)

print(maximo_comun_divisor(48,18))
