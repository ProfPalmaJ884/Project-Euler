numbers = {
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven",
    8 : "eight",
    9 : "nine",
    10 : "ten",
    11 : "eleven",
    12 : "twelve",
    13 : "thirteen",
    14 : "fourteen",
    15 : "fifteen",
    16 : "sixteen",
    17 : "seventeen",
    18 : "eighteen",
    19 : "nineteen",
    20 : "twenty",
    30 : "thirty",
    40 : "forty",
    50 : "fifty",
    60 : "sixty",
    70 : "seventy",
    80 : "eighty",
    90 : "ninety"
}

def numberGenerate(num, numeros = numbers):
    acum = 0
    for i in range(1, num + 1):
        if (i <= 20):
            acum += len(numbers[i])
        elif(i > 20 and i <= 99):
            if (i % 10 == 0):
                acum += len(numbers[i])
            else:
                decena = (i // 10 % 10)*10
                unidad = i % 10
                acum += len(numbers[decena]) + len(numbers[unidad])
        elif(i >= 100 and i <= 999):
            unidad = i % 10
            decena = (i // 10 % 10)*10
            centena = (i // 100 % 10)
            if (i % 100 == 0):
                acum += len(numbers[centena]) + 7
            elif i % 100 in numbers:
                acum += len(numbers[centena]) + len(numbers[i % 100]) + 10
            else:
                acum += len(numbers[centena]) + len(numbers[decena]) + len(numbers[unidad]) + 10
        elif(i >= 1000 and i <= 9999):
            if (i % 1000 == 0):
                acum += len(numbers[(i // 1000 % 10)]) + 8
    return acum
   
print(numberGenerate(1000))
# print(numberGenerate(99)) 854