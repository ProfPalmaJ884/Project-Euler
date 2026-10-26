def CollatzSequence(aux):
    cont = 0
    while aux > 1:
        if aux % 2 == 0:
            aux = aux // 2
        else:
            aux = (aux * 3) + 1
        cont += 1
    return cont 

def longestCollatzSequence(limit):
    largest = 0
    aux1 = 0
    for i in range (1, limit+1, 1):
        aux = CollatzSequence(i)
        if aux > aux1:
            aux1 = aux
            largest = i
    return largest

print(longestCollatzSequence(46500))