# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 23:05:10 2020

@author: zh
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if(len(strs)==0):
            return ""
        num = len(strs[0])
        for i in strs:
            if num > len(i):
                num = len(i)
        temp = ""
        result = ""
        for j in range(num):
            temp = strs[0][j]
            for i in strs:
                if(temp != i[j]):
                    return result
            result = result+temp
        return result
print (Solution().longestCommonPrefix([]))