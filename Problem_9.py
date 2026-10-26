def specialPythagoreanTriplet(n):
    for a in range (1,n):
        for b in range (a + 1 ,n):
            c = n - a - b
            if (c ** 2) == (a ** 2)+(b ** 2) and c > 0:
                return a*b*c


print(specialPythagoreanTriplet(1000))