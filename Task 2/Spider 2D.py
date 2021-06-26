#INPUTS
n = int(input())
b = input()
l= []
for i in b.split():
    l += [int(i)]

#CONSTRAINTS
if n < 2 or n > 100:
    exit()
for i in l:
    if i < 0 or i > 10**5:
        exit()
for i in l:
    if type(i) != int:
        exit()

#MAIN CODE
a = []
for i in range(len(l)-1, -1, -1):
    if len(a) == 0:
        a += [l[i]]
    else:
        if l[i] < l[i+1]:
            a += [l[i]]
        else:
            a += [l[i+1]]
sum = 0
for i in a:
    sum += i
print(sum + l[0])
            
    
