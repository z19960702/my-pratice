# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 22:08:00 2020

@author: zh
"""
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if (len(nums)<=1): 
            return len(nums)
        i = 1
        while (i != len(nums)):
            if(nums[i-1]==nums[i]):
                nums.pop(i)
            else :
                i+=1
        return i
print (Solution().removeDuplicates([1,1]))