class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        lowest=[prices[0]]
        for i in range(1,len(prices)):
            lowest.append(min(lowest[-1],prices[i]))

        for j in range(1, len(prices)):
            max_profit = max(max_profit, prices[j]-lowest[j-1])

        return max_profit

            
        