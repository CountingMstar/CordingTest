# https://school.programmers.co.kr/learn/courses/30/lessons/120924

def solution(common):
    answer = 0
    differece = []
    buffer = []

    for i in common:
        if len(buffer) < 2:
            buffer.append(i)
        if len(buffer) == 2:
            differece.append(buffer[1] - buffer[0])
            del(buffer[0])

    differece.sort()

    if differece[0] == differece[-1]:
        # print('등차수열')
        answer = common[-1] + differece[-1]
    else:
        # print('등비수열')
        rate = common[-1] / common[-2]
        answer = common[-1] * rate
    return int(answer)


# common = [1, 2, 3, 4]
common = [2, 4, 8]
sol = solution(common)
print(sol)


"""
def solution(common):
    answer = 0
    a,b,c = common[:3]
    if (b-a) == (c-b):
        return common[-1]+(b-a)
    else:
        return common[-1] * (b//a)
    return answer
"""