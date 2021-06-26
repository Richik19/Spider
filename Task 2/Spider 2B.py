#Richik Ghosh 110120092

#INPUTS
n = int(input())
q = int(input())
l = []
k = []
for i in range(q):
    a = input()
    l.append(a.split())
for i in range(n):
    k.append(i+1)

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
    if int(i[2]) < 1 or int(i[2]) > 10**9:
        exit()

#MAIN LOGIC
for i in range(len(l)):
    t = []
    for j in range(n):
        t += [0]
    ll = int(l[i][0]) - 1
    hl = int(l[i][1])
    for j in range(ll, hl):
        t[j] += int(l[i][2])
    for j in range(len(k)):
        k[j] += t[j]
print(max(k))

    
