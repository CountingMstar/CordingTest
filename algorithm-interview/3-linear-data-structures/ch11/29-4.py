class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum(s in J for s in S)


J = "aA"
S = "aAAbbbb"
solution = Solution()
count = solution.numJewelsInStones(J, S)
print(count)