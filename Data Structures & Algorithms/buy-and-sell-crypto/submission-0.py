class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        price = prices[0]

        for i in prices:
            ans = max(ans,i-price)
            price = min(price,i)

        return ans
        