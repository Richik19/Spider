def findPartition(arr, n, maxsum):
    dp = [[False for x in range(maxsum+1)] for y in range(n)]
    for i in range(n):
        dp[i][0] = True
    for i in range(1, maxsum + 1):
        dp[0][i] = arr[0] == i
    for i in range(1, n):
        for j in range(1, maxsum+1):
            if dp[i - 1][j]:
                dp[i][j] = dp[i - 1][j]
            elif j >= arr[i]: 
                dp[i][j] = dp[i - 1][j - arr[i]]
    return dp
        
#INPUTS
x = int(input())
y = int(input())
z = input()
l = z.split()
for i in range(len(l)):
    l[i] = int(l[i])
l.sort()
    
#CONSTRAINTS
if x not in [1, 2]:
    exit()
if y < 1 or y > 10**3:
    exit()
for i in l:
    if i < 0 or i > 10**3:
        exit()
s = sum(l)
if x == 1:
    print(s)
else:
    f = []
    f = findPartition(l, y, s//2) 
    k = []
    k = list(f[-1])
    k = k[::-1]
    print(s//2 - k.index(True))
