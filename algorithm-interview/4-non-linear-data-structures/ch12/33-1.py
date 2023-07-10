from typing import List


class Solution:
    def letterCombinations(digits: str) -> List[str]:
        def dfs(index, path):
            # 끝까지 탐색하면 백트래킹
            if len(path) == len(digits):
                result.append(path)
                return

            print('111111')
            print(index)
            print(len(digits))
            # 입력값 자릿수 단위 반복
            for i in range(index, len(digits)):
                print('###########')
                print(i)
                print(index)
                print(len(digits))
                print(dic[digits[i]])
                # 숫자에 해당하는 모든 문자열 반복
                for j in dic[digits[i]]:
                    print('2222222')
                    print(j)
                    dfs(i + 1, path + j)

        # 예외 처리
        if not digits:
            return []

        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
               "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        result = []
        dfs(0, "")

        return result


digits = "23"
answer = Solution.letterCombinations(digits)
print(answer)