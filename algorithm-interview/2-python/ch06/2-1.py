from typing import List
import time

start = time.time()

text1 = ["h", "e", "l", "l", "o"]
text2 = ["o", "l", "l", "e", "h"]

text = text1
# text = text2

left = 0
right = len(text)-1

while left < right:
    text[left], text[right] = text[right], text[left]
    left += 1
    right -= 1

print(text)


###########################################
class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
