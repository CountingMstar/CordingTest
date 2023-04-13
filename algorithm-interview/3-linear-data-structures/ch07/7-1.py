from typing import List
import time

nums = [2, 7, 11, 15]
target = 9

start = time.time()
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        total_sum = nums[i] + nums[j]
        if total_sum == target:
            index = [i, j]
end = time.time()
print(index)
print(f"{end - start:.10f} sec")


"""
중요
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
