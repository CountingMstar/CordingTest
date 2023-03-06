# https://school.programmers.co.kr/learn/courses/30/lessons/133502

def solution(ingredient):
    count = 0
    tmp = []
    for i in ingredient:
        tmp.append(i)
        if tmp[-4:] == [1, 2, 3, 1]:
            count += 1
            tmp = tmp[:-4]
    return count


number = [2, 1, 1, 2, 3, 1, 2, 3, 1]
answer = solution(number)
print(answer)

# def solution(ingredient):
#     count = 0
#     tmp = []
#     for i in ingredient:
#         tmp.append(i)
#         if tmp[-4:] == [1, 2, 3, 1]:
#             count += 1
#             tmp = tmp[:-4]
#     return count


# number = [2, 1, 1, 2, 3, 1, 2, 3, 1]
# answer = solution(number)
# print(answer)