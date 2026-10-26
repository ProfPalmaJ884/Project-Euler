def primeSummation(n):
    es_primo = [True] * (n)
    es_primo[0] = es_primo[1] = False
    
    for p in range(2, int(n**0.5)):
        if es_primo[p]:
            for i in range(p * p, n, p):
                es_primo[i] = False
              
    primos = [i for i in range(2, n) if es_primo[i]]
    return sum(primos)

resultado = primeSummation(2000000)

print(f"La suma de los primos menores a 2000000 es: {resultado}")