# https://school.programmers.co.kr/learn/courses/30/lessons/181187


def solution(r1, r2):
    answer = 0
    max_y = r2
    min_y = r1

    for x in range(0, r2+1):

        while True:
            d = max_y**2 + x**2
            if d <= r2**2:
                break
            max_y -= 1

        while True:
            d = min_y**2 + x**2
            if d < r1**2:
                min_y += 1
                break
            
            if min_y == 0:
                min_y += 1
                break

            min_y -= 1


        tmp = max_y - min_y + 1
        answer += tmp

    answer *= 4
    return answer

answer = solution(2, 3)
print(answer)