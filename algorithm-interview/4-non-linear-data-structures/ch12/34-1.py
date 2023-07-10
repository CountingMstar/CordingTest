from typing import List


class Solution:
    def permute(nums: List[int]) -> List[List[int]]:
        results = []
        prev_elements = []

        def dfs(elements):
            # 리프 노드일때 결과 추가
            if len(elements) == 0:
                results.append(prev_elements[:])
                print('666666666')
                print(results)

            print('00000000')
            print(elements)

            # 순열 생성 재귀 호출
            for e in elements:
                print('111111111')
                print(e)
                print(elements[:])

                print('222222222')
                next_elements = elements[:]
                print(next_elements)
                next_elements.remove(e)
                print(next_elements)
                
                print('33333333333')
                print(prev_elements)
                prev_elements.append(e)
                print(prev_elements)
                dfs(next_elements)
                prev_elements.pop()
                print(prev_elements)

        dfs(nums)
        return results


nums = [1, 2, 3]
answer = Solution.permute(nums)
print(answer)
