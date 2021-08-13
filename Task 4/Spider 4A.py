#FUNCTIONS
from collections import defaultdict
 
class graph:
    def __init__(self, n):
        self.v = n
        self.graph = defaultdict(list)
        
    def addedge(self, u, v):
        self.graph[u].append(v)
        
    def DFS(self, s):
        vis = set()
        cnt = [0]
        r = 0
        self.DFShelp(s, vis, cnt, r)
        return cnt[0]

    def DFShelp(self, u, vis, cnt, r):
        vis.add(u)
        r +=1 
        if r == (self.v):
            cnt[0] += 1
        else:
            for i in self.graph[u]:
                if i not in vis:
                    self.DFShelp(i, vis, cnt, r)
        vis.remove(u)
        r -= 1

#INPUTS
x = input()
l = x.split()
for i in range(len(l)):
    l[i] = int(l[i])
n = l[0]
m = l[1]
f = []
for i in range(m):
    y = input()
    k = y.split()
    for j in range(2):
        k[j] = int(k[j]) - 1
    f += [k]
#CONSTRAINTS
if n < 2 or n > 8 :
    exit()
if l[1] < 0 or l[1] > (n*(n-1))/2:
    exit()
        
#MAIN CODE
temp = []
for i in range(len(f)):
    for j in range(len(f[i])):
        if f[i][j] not in temp:
            temp += [f[i][j]] 
temp1 = [i for i in range(n)]
temp.sort()
if temp != temp1:
    print(0)
else:
    final = graph(n)
    for i in range(len(f)):
        final.addedge(f[i][0], f[i][1])
        final.addedge(f[i][1], f[i][0])
    k = final.DFS(0)
    print(k)
