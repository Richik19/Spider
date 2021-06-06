#INPUTS

x = int(input())
l=[]
for i in range(x):
    y = int(input())
    l.append(y)

#CONSTRAINTS

if x > 5 and x < 1:
    exit()
for i in l:
    if i > 500 and i < 3:
        exit()
for i in l:
    if i % 2 == 0:
        exit()
if x != len(l):
    exit()

#MAIN CODE
    
for i in l:
    for a in range(0, int((i-1)/2)):
        if a == 0:
            print("*" * i)
        else:
            print("*" * int((i-(2*a-1))/2) + " " * (2*a -1) + "*" * int((i-(2*a-1))/2))
    for a in range(int((i-1)/2), -1, -1):
        if a == 0:
            print("*" * i)
        else:
            print("*" * int((i-(2*a-1))/2) + " " * (2*a -1) + "*" * int((i-(2*a-1))/2))

