#Binary to Decimal Function
def btd(b):
    return int(b,2)

#Decimal to Binary Function
def dtb(d):
    return bin(d)
    
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

dn = btd(y)
if dn <= 0:
    print(-1)
else:
    hn = dn + 1
    ln = dn - 1
    a = dtb(hn)
    b = dtb(ln)
    nb = ""
    if len(a) != x + 2:
        print(-1)
    else:
        if len(b) == x + 2:
            print(b[2:] + " " + a[2:])
        else:
            diff = x + 2 - len(b)
            nb = "0" * diff + b[2:]
            print(nb + " " + a[2:])

    







