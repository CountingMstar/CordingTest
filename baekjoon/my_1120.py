a, b = input().split()

def score(a, b):
    s = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            s += 1
    return s

scores = []
for i in range(len(b)-len(a)+1):
    bb = b[i:i+len(a)]
    scores.append(score(a, bb))

# ind = scores.index(min(scores))
print(min(scores))

    

