from typing import List


class Solution:
    def permute(nums: List[int]) -> List[List[int]]:
        results = []
        prev_elements = []

        def dfs(elements):
            
            for i in elements:
                prev_elements.append(i)
                



        dfs(nums)
        return results


nums = [1, 2, 3]
answer = Solution.permute(nums)
print(answer)
