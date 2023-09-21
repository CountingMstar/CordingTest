N = input()
a = list(map(int,input().split()))
b = list(map(int,input().split()))

# a = [4, 2, 5, 6]
# a = sorted(a)
# b = a[::-1]
# print(a)
# print(b)

a = sorted(a)
b = sorted(b)[::-1]

answer = 0
for i in range(int(N)):
    answer += a[i]*b[i]

print(answer)
