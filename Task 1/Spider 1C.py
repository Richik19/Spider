#Richik Ghosh 110120092

#INPUTS
a = input()
b = input()
c = input()

d = a.split()
e = b.split()
f = c.split()

n = int(d[0])
r = int(d[1])
x = int(d[2])
y = int(d[3])

#CONSTRAINTS

if n > 100000 and n < 1:
    exit()
if r > 3000 and r < 1:
    exit()
if x > 100 and x < 1:
    exit()
if y > 100 and y < 1:
    exit()
if len(e) != n:
    exit()
if len(f) != n:
    exit()
for i in e:
    if int(i) not in [0,1]:
        exit()
for i in f:
    if int(i) not in [0,1]:
        exit()

#MAIN CODE

gd, bd = 0, 0
for i in range(0,n):
    if int(e[i]) == 1:
        if int(f[i]) == 1:
            gd += 1
        else:
            bd += 1
    else:
        pass
net = x * gd - y * bd
if net > 0:
    print("promoted")
elif net < 0:
    print("demoted")
else:
    print("no change")
    
    


