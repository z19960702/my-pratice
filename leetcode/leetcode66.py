# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 11:15:29 2020

@author: zh
"""
from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1,-1,-1):
            if (digits[i]+1<10):
                digits[i] +=1
                break
            else : 
                digits[i] = 0
                if(i ==0 ):
                    digits.insert(0,1)
        return digits
print (Solution().plusOne([9]))
        