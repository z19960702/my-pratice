# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 11:06:02 2020

@author: zh
"""
from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #尾插法
        i = 1
        j = 1
        k = 1
        while(j<=n):
            if (m - i<0):
                for t in range (n- j + 1):                  
                    nums1[t] = nums2[t]
                break
            if(nums1[m-i]>=nums2[n-j]):
                nums1[m+n-k] = nums1[m-i]
                i+=1
            else:
                nums1[m+n-k] = nums2[n-j]
                j+=1
            k+=1
            
        print (nums1)
Solution().merge([4,5,6,0,0,0],3,[1,2,3],3)