def multiplesOf3Or5(number):
    sum = 0
    for i in range (1, number):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

print(multiplesOf3Or5(19564))