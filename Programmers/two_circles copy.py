"""
input = ["X591X","X1X5X","X231X", "1XXX1"]

for map in input:
    print(map)
    print(map[0])
    print(len(map))





    # for m in map:
    #     i
    #     if m == 'X':

    #     if m == '1' or m == '2'or m == '3'or m == '4'or m == '5'or m == '6'or m == '7'or m == '8'or m == '9':
    #         islands.append(int(m))
    #         island = int(m)

        


def solution(maps):
    answer = []
    return answer

answer = solution(input)
print(answer)
"""

import torch

a = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]])
b = [4, 8]
print(a.shape)
print(a)

k = int(b[0]/a.shape[0])
a = a.tolist()

tmp2 = []
for i_ in range(len(a)):
    tmp1 = []
    i = a[i_]
    for j_ in range(len(i)):
        j = i[j_]
        for _ in range(k):
            tmp1.append(j)

    for _ in range(k):
        tmp2.append(tmp1)
    
a = torch.tensor(tmp2)
print(a.shape)
print(a)

# window size
pad_len = 3

import torch.nn.functional as F
a = F.pad(a, (pad_len, pad_len, pad_len, pad_len), "constant", 0)
print(a.shape)
print(a)

a = a.tolist()
print(a)
new_a = []
for i in range(pad_len, pad_len+b[0]):
    tmp = []
    for j in range(pad_len, pad_len+b[1]):
        window = []
        
        for i_ in range(i-pad_len, i+pad_len+1):
            for j_ in range(j-pad_len, j+pad_len+1):
                window.append(a[i_][j_])

        tmp.append(sum(window)/len(window))
    new_a.append(tmp)

new_a = torch.tensor(new_a)
print(new_a.shape)
print(new_a)


    








