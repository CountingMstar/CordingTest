a = 'apple'

print(a)
print(len(a))

b = ''
for i in range(1, len(a)+1):
    n = len(a) - i
    b += a[n]

print(b)

c = ''.join(reversed(a))
print(c)
