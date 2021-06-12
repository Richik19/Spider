#Richik Ghosh 110120092

#INPUTS

x = int(input())
y = input()

#CONSTRAINTS

if x > 100000:
    exit()
for i in y:
    if int(i) != 0 and int(i) != 1:
        exit()
if x != len(y):
    exit()

#MAIN LOGIC

dn = int(y, 2)
if dn <= 0:
    print(-1)
else:
    hn = dn + 1
    ln = dn - 1
    a = bin(hn)
    b = bin(ln)
    nb = ""
    if len(a) != x + 2 or len(b) != x + 2:
        print(-1)
    else:
        print(b[2:] + " " + a[2:])
     

    







