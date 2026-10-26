def powerDigitSum(exponent):
    power = 2 ** exponent
    suma = 0
    aux = list(str(power))
    for digits in aux:
        suma = int(digits) + suma
    print(suma)



powerDigitSum(8)