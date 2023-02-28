# https://school.programmers.co.kr/learn/courses/30/lessons/120910

def solution(n, t):
    # 제곱
    answer = n * (2 ** t)
    # answer = n * (pow(2, t))
    return answer

# n_t = [2, 10]
n_t = [7, 15]
n = n_t[0]
t = n_t[1]
number = solution(n, t)
print(number)


"""
def solution(n, t):
    return n << t

비트 쉬프트 연산: n << t == n * 2^t
"""