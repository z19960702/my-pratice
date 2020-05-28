# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 10:51:12 2020

@author: zh
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 1
        for i in range (1,n):
            temp = a+b
            a = b
            b = temp
        return b
print (Solution().climbStairs(5))