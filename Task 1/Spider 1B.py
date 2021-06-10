#Richik Ghosh 110120092

#IMPORTS
import math

#INPUTS

x = int(input())
y = input()

#CONSTRAINTS

if x > 100000 and x < 1:
    exit()
if (math.log2(x)).is_integer() == False:
    exit()
if y.islower() == False:
    exit()
if x != len(y):
    exit()

#MAIN CODE
    
if x == 1:
    print(0)
else:
    count = 0
    while int(x) > 0:
        x = x / 2
        if y[:int(x)] == y[int(x):int(x*2)]:
            count += 1
    print(count)
        
