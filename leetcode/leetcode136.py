# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 22:29:08 2020

@author: zh
"""
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range (1,len(nums)):
            nums[i] = nums[i]^nums[i-1]
        return nums[len(nums)-1]
print (Solution().singleNumber([1,1,2,2,3,3,4]))
            