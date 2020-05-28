# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 22:31:39 2020

@author: zh
"""
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range (1,len(nums)):
            nums[i] = max(nums[i],nums[i-1]+nums[i])
        return max(nums)
print (Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
        