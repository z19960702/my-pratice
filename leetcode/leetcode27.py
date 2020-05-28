# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 22:30:41 2020

@author: zh
"""
from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if (len(nums) == 0):
            return 0
        j = len(nums)-1
        i = 0
        while (i<=j):
            if (nums[i]==val):
                nums[i] = nums[j]
                j-=1
            else : 
                i+=1
        return i
print (Solution().removeElement([3,3],3))