class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min = prices[0]
        profit,max_profit  = 0 , 0  
        for i in range (1,len(prices)) :
            if prices [i] < min :
                min = prices[i]
            profit = prices[i] - min
            max_profit = max (max_profit,profit)
        return max_profit
