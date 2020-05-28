# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 19:35:21 2020

@author: zh
"""
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sum =0
        if (len(prices)==0):
            return 0
        min = prices[0]
        
        for i in range (1,len(prices)):
            if (min > prices[i]):
                min = prices[i]
            if (prices[i] - min > sum):
                sum = prices[i] - min
        return sum
print (Solution().maxProfit([1]))
        