import collections


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        freqs = collections.Counter(S)  # 돌(S) 빈도 수 계산
        count = 0

        print(freqs)

        # 비교 없이 보석(J) 빈도 수 합산
        for char in J:
            count += freqs[char]

        return count


J = "aA"
S = "aAAbbbb"
solution = Solution()
count = solution.numJewelsInStones(J, S)
print(count)