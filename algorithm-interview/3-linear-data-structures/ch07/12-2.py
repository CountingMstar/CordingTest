import sys
from typing import List
import time
start = time.time()

prices = [7, 1, 5, 3, 6, 4]
min_price = sys.maxsize
max_profit = -sys.maxsize
print(min_price)

for price in prices:
    min_price = min(min_price, price)
    profit = price - min_price
    max_profit = max(max_profit, profit)

end = time.time()
print(max_profit)
print(f"{end - start:.10f} sec")


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize

        # 최소값과 최대값 계속 갱신
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)

        return profit
