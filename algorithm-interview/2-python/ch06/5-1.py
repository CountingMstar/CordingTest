import collections
from typing import List
import time

start = time.time()
text1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
text = text1

# 존재하지 않는 Key에도 KeyError가 발생하지않는 dictionary
anagrams = collections.defaultdict(list)

for word in text:
    # 문자를 알파벳 순서대로 정렬
    sorted_word = sorted(word)
    print(sorted_word)
    # 문자 리스트를 문자로 합침
    sorted_word = ''.join(sorted_word)
    print(sorted_word)

    anagrams[sorted_word].append(word)

print(anagrams)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)

        for word in strs:
            # 정렬하여 딕셔너리에 추가
            anagrams[''.join(sorted(word))].append(word)
        return list(anagrams.values())
