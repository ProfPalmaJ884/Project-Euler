def es_primo(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        aux = int(n ** 0.5)
        for i in range (3, aux + 1 , 2):
            if n % i == 0:
                return False
        return True

def nthPrime(n):
    count = 1
    num = 3
    while count < n: 
        if es_primo(num):
            count += 1
        if count == n:
            return num
        num +=2   

print(nthPrime(1000))
