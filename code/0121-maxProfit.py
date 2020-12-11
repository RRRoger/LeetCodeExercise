# -*- coding: utf-8 -*-

# 暴力求解

# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         ans = 0
#         for i in range(len(prices)):
#             for j in range(i + 1, len(prices)):
#                 if prices[j] - prices[i] > ans:
#                     ans = prices[j] - prices[i]
#         return ans


class Solution:
    def maxProfit(self, prices):
        inf = int(1e9)
        minprice = inf
        maxprofit = 0
        for price in prices:

            print(price, minprice, maxprofit, price - minprice)

            maxprofit = max(price - minprice, maxprofit)
            minprice = min(price, minprice)
        return maxprofit


if "__main__" == __name__:
    solution = Solution()

    print(solution.maxProfit([7,1,5,3,6,4,100,0]))

    print(solution.maxProfit([]))




