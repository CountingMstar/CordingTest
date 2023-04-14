from typing import List
import time

input = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# input = [2, 0, 1, 0, 3]
volume = 0
left, right = 0, len(input)-1
left_max = input[left]
right_max = input[right]

while left < right:
    left_max = max(left_max, input[left])
    right_max = max(right_max, input[right])

    if left_max <= right_max:
        v = left_max - input[left]
        volume += v
        left += 1
    else:
        v = right_max - input[right]
        volume += v
        right -= 1

print('############')
print(volume)



class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max, right_max = max(height[left], left_max), max(height[right], right_max)
            # 더 높은 쪽을 향해 투 포인터 이동
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1
        return volume

volume = Solution().trap(input)
print(volume)
