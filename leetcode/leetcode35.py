# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 23:02:44 2020

@author: zh
"""
from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0 
        j = len(nums)-1
        while (i<j):
            if (target< nums[(i+j)//2]):
                j = (i+j)//2-1
            elif (target == nums[(i+j)//2]):
                return (i+j)//2
            else:
               i = (i+j)//2+1
        if nums[i]<target:
            return i+1
        else :
            return i

print (Solution().searchInsert([1,3,5,6],0))      
                