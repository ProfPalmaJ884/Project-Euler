def largestPrimeFactor(number):
    aux = 2
    while number > aux:
        if number % aux == 0:
            number = number/aux
        else:
            aux += 1
    return aux

print(largestPrimeFactor(18))