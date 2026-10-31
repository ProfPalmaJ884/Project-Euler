#1 2 3 5 8 13 21 34 55
def fiboEvenSum(lim):
    n = 0
    next = 1
    prev = 0
    acum = 0
    while n <= lim:
       if n % 2 == 0:
                acum += n
       n = prev + next
       prev = next
       next = n
    return acum


print(fiboEvenSum(4000000))
