#Richik Ghosh 110120092
#FUNCTIONS
def CancerTiles(arr, n, k):
    fw = [0 for i in range(n)]
    bw = [0 for i in range(n)]
    cur_sum, max_sum = arr[0], arr[0]

    fw[0] = cur_sum
    for i in range(1,n):
        cur_sum = max(arr[i], cur_sum + arr[i])
        max_sum = max(max_sum, cur_sum)
        fw[i] = cur_sum

    cur_sum = max_sum = bw[n-1] = arr[n-1]
    i = n-2
    while i >= 0:
        cur_sum = max(arr[i], cur_sum + arr[i])
        max_sum = max(max_sum, cur_sum)
        bw[i] = cur_sum
        i -= 1
        
    ans = max_sum
    for i in range(1,k+1):
        for j in range(1, n-i):
            ans = max(ans, max(0,fw[j - 1]) + max(0, bw[i + j]))
        if ans == 0:
            p = [i for i in range(arr, arr + n)]
            return(max(p))
    return ans
  
#INPUTS
x = input()
l = x.split()
n = int(l[0])
k = int(l[1])
y = input()
l = y.split()
for i in range(len(l)):
    l[i] = int(l[i])
print(CancerTiles(l, n, k))
 
