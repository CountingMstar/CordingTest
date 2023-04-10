import time

start = time.time()

text1 = "A man, a plan, a canal: Panama"
text2 = "race a car"

text = text1
# text = text2
strs = []
for char in text:
    # print(char)
    # isalnum() : 영문자, 숫자 여부 판단
    if char.isalnum():
        strs.append(char.lower())
        print(strs)

while len(strs) > 1:
    # strs.pop(0) : 맨 앞부분 뽑기
    # strs.pop() : 맨 뒷부분 뽑기
    if strs.pop(0) != strs.pop():
        print('False')

    else:
        print('True')
    
end = time.time()
print(f"{end - start:.5f} sec")



##############################################
class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        # 팰린드롬 여부 판별
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False

        return True
