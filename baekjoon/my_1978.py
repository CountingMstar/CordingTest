import math

N = int(input())
L = list(map(int,input().split()))

def sosu(x):
    if x == 1:
        return False
        exit()

    if x == 2:
        return True
        exit()
    
    for i in range(2, int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
            exit()

    return True
        
# print(sosu(7))

sum = 0
for i in L:
    if sosu(i) == True:
        sum += 1

print(sum)



