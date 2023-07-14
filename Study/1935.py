import sys

# sys.stdin.readline() : input()보다 빠름
N = int(sys.stdin.readline())
postfix = sys.stdin.readline()[:-1]
num = [int(sys.stdin.readline()) for _ in range(N)]

stack = []

for i in postfix:
    
    # i.isalpha() : i가 알파벳인가?
    # ord('A') : A의 아스키코드 숫자
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

# '%0.2f' : 소숫점 둘째자리까지
print('%0.2f'%stack[0])