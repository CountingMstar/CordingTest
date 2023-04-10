import re

text1 = "A man, a plan, a canal: Panama"
text2 = "race a car"

text = text1
# text = text2

text = text.lower()
print(text)
# 불필요한 문제 제거
# re.sub(불필요한 문자, 대체할 문자, 수정할 문장)
text = re.sub('[-=+,#/\?:^.@*\"※~ㆍ!』‘|\(\)\[\]`\'…》\”\“\’·]', '', text)
# 띄어쓰기 공백 지우기
text = re.sub(r"\s", "", text)
print('################')
print(text)

inverse_text = text[::-1]
print(inverse_text)

if text == inverse_text:
    print('True')
else:
    print('False')


    
##############################################
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        # 정규식으로 불필요한 문자 필터링
        s = re.sub('[^a-z0-9]', '', s)

        return s == s[::-1]  # 슬라이싱
