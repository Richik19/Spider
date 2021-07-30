#Richik Ghosh 110120092

#FUNCTIONS
def prime(n):
   prm = [True for i in range(n+1)]
   p = 2
   while(p * p <= n):
      if (prm[p] == True):
         for i in range(p * p, n + 1, p):
            prm[i] = False
      p += 1
   c = 0
   for p in range(2, n+1):
      if prm[p]:
         c += 1
   return c

#INPUTS
x = int(input())

#CONSTRAINTS
if x < 2 or x > 10**5:
    exit()

#MAIN CODE
count = prime(x)
sum = 0
for i in range(count+1):
   sum += i
print(sum)
