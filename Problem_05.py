def smallestMult(n):
   num = n
   while True:
      flag = True
      for i in range (n // 2, n + 1):
         if num % i != 0:
            flag = False
            break
      if flag:
         return num
      else:
         num +=n
      

print(smallestMult(20))
