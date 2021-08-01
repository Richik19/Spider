#FUNCTIONS
def WW(mid, l, k):
    s1 = 0
    sub = 0
    n = len(l)
    for i in range(n):
        if l[i] > mid:
            return False
        if s1 + l[i] <= mid:
            s1 += l[i]
        else:
            sub += 1
            s1 = l[i]
    sub += 1
    return (k >= sub)


#INPUTS
x = int(input())
y = int(input())
z = input()
l = z.split()
for i in range(y):
    l[i] = int(l[i])
    
#CONSTRAINTS
if x < 1 or x > y:
    exit()
if y < 1 or y > 10**5:
    exit()
for i in l:
    if i < 0 or i > 10**9:
        exit()

#MAIN CODE
if x == 1:
    print(sum(l))
else:
    left = max(l)
    right = sum(l)
    while left < right:
        mid = (left+right)//2
        if WW(mid, l, x):
            right = mid
        else:
            left = mid + 1
    print(int(left))

    
        
        
        
