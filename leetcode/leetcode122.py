# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 22:18:52 2020

@author: zh
"""
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sum =0
        if (len(prices)==0):
            return 0
        for i in range (1,len(prices)):
            if (prices[i-1] < prices[i]):
                sum +=(prices[i] - prices[i-1])
        return sum
print (Solution().maxProfit([7,6,4,3,1]))
        