# https://school.programmers.co.kr/learn/courses/30/lessons/120923

def solution(num, total):
    answer = []
    bias = ((num - 1) * num) / 2
    x = (total - bias) / num

    for i in range(num):
        element = x + i
        answer.append(int(element))

    return answer


num_total = [3, 12]
# num_total = [5, 15]
num = num_total[0]
total = num_total[1]
answer = solution(num, total)
print(answer)


"""
def solution(num, total):
    return [(total - (num * (num - 1) // 2)) // num + i for i in range(num)]
"""