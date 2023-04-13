from typing import List
import time

nums = [2, 7, 11, 15]
target = 9

start = time.time()
for i, n in enumerate(nums):
    complement = target - n

    if complement in nums[i+1:]:
        j = nums.index(complement)
        index = [i, j]
end = time.time()
print(index)
print(f"{end - start:.10f} sec")

"""
중요
for i, n in enumerate(nums):
    complement = target - n

    if complement in nums[i+1:]:
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            complement = target - n

            if complement in nums[i + 1:]:
                return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]
