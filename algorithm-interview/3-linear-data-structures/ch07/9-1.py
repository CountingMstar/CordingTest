from typing import List
import time
start = time.time()
nums = [-1, 0, 1, 2, -1, -4]
nums.sort()
results = []

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        for k in range(j+1, len(nums)):
            total_sum = nums[i] + nums[j] + nums[k]
            if total_sum == 0:
                result = [nums[i], nums[j], nums[k]]
                result.sort()
                if result not in results:
                    results.append(result)

end = time.time()
print(results)
print(f"{end - start:.10f} sec")

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()

        # 브루트 포스 n^3 반복
        for i in range(len(nums) - 2):
            # 중복된 값 건너뛰기
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 1):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                for k in range(j + 1, len(nums)):
                    if k > j + 1 and nums[k] == nums[k - 1]:
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        results.append([nums[i], nums[j], nums[k]])

        return results
