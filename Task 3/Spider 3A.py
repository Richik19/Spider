#110120092 Richik Ghosh

#INPUTS
x = int(input())

#CONSTRAINTS
if x < 0 or x > 10**100000:
    exit()

#MAIN CODE
l = [int(i) for i in str(x)]
h = sum(l)
count = 0
while len(str(h)) > 1:
    count += 1
    l = [int(i) for i in str(h)]
    h = sum(l)
print(count+1)
