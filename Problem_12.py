#Highly Divisible Triangular Number

def divisibleTriangleNumber(n):
    i = 1 #Contador para generar los numeros

    while True: #Ciclo infinito que termina al encontrar el numero
        numero_tri = int(i * (i + 1) /2) #Generamos un numero trigualar iniciando en i = 1
        limite = int(numero_tri ** 0.5) #Calculamos la raiz cuadrada del numero para hallar los divisores en menos intentos
        aux = 0 #Contenedor temporal de los divisores de cada numero 

        for j in range(1, limite + 1): #Ciclo para buscar los divisores del numero
            if numero_tri % j == 0: #Si el numero generado es divisor del numero
                if j * j == numero_tri: #Si es un cuadrado prefecto se suma un solo divisor porque el factor se multiplica asi mismo
                    aux += 1
                else: #Sino es cuadrado perfecto se suman dos divisores: El divisor actual (j) y su cociente correspondiente (numero_tri // j).
                    aux += 2
        if aux > n: #si los divisores encontrados son mayores a los divisore buscados (n)
            return numero_tri #Rompemos el ciclo y retornamos el numero triangular
        
        i += 1 #Incrementamos en una unidad para calcular el siguiente numero

print(divisibleTriangleNumber(500))
        

