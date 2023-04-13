from typing import List
import time

input = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
input = [2, 0, 1, 0, 3]
input = [1, 0, 3]

print(input.index(max(input)))

max_index = input.index(max(input))
window = []
window.append(input[max_index])
water = 0 
#left
for i in range(max_index):
    if len(window) == 2:
        window.remove(window[0])
    index = max_index - (i + 1)
    value = input[index]
    window.append(value)
    print(window)

    if window[0] < window[1]:
        wall_index = index + 1
        print('=============')
        print(window[1])
        print(input[wall_index])
        while True:
            print('*******')
            water += (window[1] - input[wall_index])
            wall_index = index + 1
            print(window[1])
            print(input[wall_index])
            if window[1] > input[wall_index]:
                break

print('#######')


print(water)
    




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
