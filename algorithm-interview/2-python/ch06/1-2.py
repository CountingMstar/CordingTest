import collections
from typing import Deque

import time

start = time.time()

text1 = "A man, a plan, a canal: Panama"
text2 = "race a car"

text = text1
# text = text2

# 자료형 데크로 선언
strs: Deque = collections.deque()

for char in text:
    # print(char)
    # isalnum() : 영문자, 숫자 여부 판단
    if char.isalnum():
        strs.append(char.lower())
        print(strs)

while len(strs) > 1:
    # strs.pop(0) : 맨 앞부분 뽑기
    # strs.pop() : 맨 뒷부분 뽑기
    if strs.popleft() != strs.pop():
        print('False')

    else:
        print('True')
    
end = time.time()
print(f"{end - start:.5f} sec")



##############################################
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 자료형 데크로 선언
        strs: Deque = collections.deque()

        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False

        return True
