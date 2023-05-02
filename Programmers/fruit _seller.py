# https://school.programmers.co.kr/learn/courses/30/lessons/135808?language=python3

def solution(k, m, score):
    answer = 0
    total_score = 0
    score.sort(reverse=True)
    new_m = m

    while True:
        try:
            total_score += score[m-1]
            m += new_m 
        except:
            break

    answer = total_score*new_m
    return answer


# k = 3
# m = 4
# score = [1, 2, 3, 1, 2, 3, 1]
k = 4
m = 3
score = [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]
answer = solution(k, m, score)
print(answer)