import collections
import re
from typing import List
import time

start = time.time()

text1 = "Bob hit a ball, the hit BALL flew far after it was hit."

paragraph = text1

# 구두점등 불필요한 문자 제거
words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split()]
print(words)

# Counter()를 이용해 반복된 단어수 체크
counts = collections.Counter(words)
print(counts)
print(counts.most_common(1)[0][0])

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
            .lower().split()
                 if word not in banned]

        counts = collections.Counter(words)
        # 가장 흔하게 등장하는 단어의 첫 번째 인덱스 리턴
        return counts.most_common(1)[0][0]
