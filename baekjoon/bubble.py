a = [40, 20, 5, 10, 8]

for j in range(len(a)-1):
    for i in range(len(a)-1-j):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]

print(a)

# for j in range(len(a)-1):
#     for i in range(len(a)-1-j):
#         tmp = []
#         tmp.append(a[i])
#         tmp.append(a[i+1])

#         if tmp[0] > tmp[1]:
#             tmp = tmp[::-1]

#         a[i] = tmp[0]
#         a[i+1] = tmp[1]

# print(a)
    

    
    


