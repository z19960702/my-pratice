# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 13:27:49 2020

@author: zh
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        if (x == 0 or x == 1):
            return x
        #if (x == 1 or x==2 or x==3):
        #    return 1
        for i in range (1,x//2+1):
            if (i*i == x):
                return i
            if (i*i>x):
                return i-1
        return i
            
print (Solution().mySqrt(9))