class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        i = 0
        while i < len(prices) - 1:
            while prices[i] <= prices[i + 1]:
                res += prices[i + 1] - prices[i]
                i += 1
                print(i)
                if i == len(prices) - 1:
                    break
            else:
                i += 1
            print()
        
        return res