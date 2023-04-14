from typing import List
import time
start = time.time()

prices = [7, 1, 5, 3, 6, 4]


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price = 0

        for i, price in enumerate(prices):
            for j in range(i, len(prices)):
                max_price = max(prices[j] - price, max_price)

        return max_price

max_profit = Solution().maxProfit(prices)
end = time.time()
print(max_profit)
print(f"{end - start:.10f} sec")