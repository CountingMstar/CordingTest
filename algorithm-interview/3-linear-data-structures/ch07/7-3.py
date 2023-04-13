from typing import List
import time

nums = [2, 7, 11, 15]
target = 9
nums_map = {}
start = time.time()
for i, n in enumerate(nums):
    nums_map[n] = i

for i, n in enumerate(nums):
    complement = target - n
    if complement in nums_map:
        j = nums_map[complement]
        if i < j:
            index = [i, j]

end = time.time()
print(index)
print(f"{end - start:.10f} sec")

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        # 키와 값을 바꿔서 딕셔너리로 저장
        for i, num in enumerate(nums):
            nums_map[num] = i

        # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return [i, nums_map[target - num]]
