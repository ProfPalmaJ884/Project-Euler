def es_palindromo(num):
    numero = str(num)
    aux = numero[::-1]
    return numero == aux

def tres_tres():
    mayor = 0
    for i in range(100, 1000):
        for j in range(i, 1000):
            if es_palindromo(i*j):
                aux = i*j
                if aux > mayor:
                    mayor = aux
    return mayor
            

        

print(es_palindromo(1001))
print(tres_tres())
