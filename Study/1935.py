import sys

N = int(sys.stdin.readline())
postfix = sys.stdin.readline()[:-1]
num = [int(sys.stdin.readline()) for _ in range(N)]

stack = []

for i in postfix:
    
    if i.isalpha():
        stack.append(num[ord(i) - ord('A')])

    else:
        b = stack.pop()
        a = stack.pop()

        if i == '+':
            stack.append(a+b)
        if i == '-':
            stack.append(a-b)
        if i == '*':
            stack.append(a*b)
        if i == '/':
            stack.append(a/b)

print('%0.2f'%stack[0])