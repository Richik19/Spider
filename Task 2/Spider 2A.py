#INPUTS
t = int(input())
l=[]
for i in range(t):
    a = input()
    l.append(a)

#CONSTRAINTS
if t < 1 or t > 500:
    exit()
for i in l:
    if len(i) < 1 or len(i) > 10**6:
        exit()

#MAIN CODE
for i in l:
    sum = 0
    count = 0
    for j in range(len(i)):
        if i[j] == "<":
            sum += 1
        else:
            sum -= 1
        if sum < 0:
            break
        if sum == 0:
            count = 1 + j
    print(count)
