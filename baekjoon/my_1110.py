import sys

input = sys.stdin.readline

N = input()
i = 0

if len(N) == 2:
    N = '0' + N

original = N[:-1]

while True:
    n0 = N[0]
    n1 = N[1]

    new = str(int(n0) + int(n1))[-1]
    N = n1 + new
    i += 1

    if N == original:
        print(i)
        break





