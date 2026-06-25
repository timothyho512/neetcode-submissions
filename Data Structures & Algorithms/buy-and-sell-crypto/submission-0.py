class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        left = 0
        while left < len(prices):
            right = left + 1
            while right < len(prices):
                if prices[right] < prices[left]:
                    break

                ans = max(ans, prices[right] - prices[left])
                right += 1

            left = right
        return ans