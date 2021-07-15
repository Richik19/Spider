#Richik Ghosh 110120092

#INPUTS
n = int(input())
q = int(input())
l = []
k = [i+1 for i in range(n)]
for i in range(q):
    a = input()
    l += [a.split()]
   
#CONSTRAINTS
if n < 1 or n > 10**5:
    exit()
if q < 1 or q > 10**5:
    exit()
for i in l:
    if int(i[0]) < 1 or int(i[0]) > n:
        exit()
    if int(i[1]) < 1 or int(i[1]) > n:
        exit()
    if int(i[2]) > 10**9:
        exit()

#MAIN LOGIC
p = [0 for i in range(n)]
for i in range(q):
    x, y = int(l[i][0]),int(l[i][1])
    p[x-1] += int(l[i][2])
    if y < n:
        p[y] -= int(l[i][2])
for i in range(1,n):
    p[i] += p[i-1]
for i in range(n):
    p[i] += k[i]
print(max(p))
