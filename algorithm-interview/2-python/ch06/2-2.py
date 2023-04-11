from typing import List
import time

start = time.time()

text1 = ["h", "e", "l", "l", "o"]
text2 = ["o", "l", "l", "e", "h"]

text = text1
# text = text2

text.reverse()

end = time.time()
print(f"{end - start:.5f} sec")
print(text)



###########################################
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()
