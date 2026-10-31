#Usando las formulas de Gauss para sumar numeros triangulares:
def sumSquareDifference1(n):
    suma = (0.5) * (n + 1) * n
    suma_cuadrados = (n*(n+1)*(2*n+1))/6
    result = (suma * suma) - suma_cuadrados
    return int(result)

#Usando for:
def sumSquareDifference2(n):
    suma = 0
    suma_cuadrados = 0
    for i in range(n + 1):
        suma += i
        suma_cuadrados += i*i
    result = (suma * suma) - suma_cuadrados
    return int(result)

print(sumSquareDifference1(100))
print(sumSquareDifference2(100))
