#Fibnocci function
def fib(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a

#INPUTS
a = input()
l = [int(i) for i in a.split()]
n = l[0]
m = l[1]
bsteps = []
for i in range(m):
    x = int(input())
    if x < 1 or x > n-1:   #CONSTRANT
       exit()
    bsteps += [x]
bsteps.sort()
steps = []
steps = [0] + bsteps + [n]
    
#CONSTRAINTS
if n < 1 or n > 10**5:
    exit()
if m < 0 or m > n - 1:
    exit()

#MAIN CODE

gsteps = []
for i in range(len(steps)-1):
    temp = []
    for j in range(steps[i]+1, steps[i+1]):
        temp += [j]
    gsteps.append(temp)
gsteps[0] = [0] + gsteps[0]
gsteps[-1] = gsteps[-1] + [n]
count = 1
for i in range(0, len(bsteps)-1):
    if bsteps[i+1] - bsteps[i] == 1:
        count = 0
        print(0)
        exit()
for i in gsteps:
    if len(i) >= 2:
        count *= fib(len(i))
        count %= 1000000007
print(count)
