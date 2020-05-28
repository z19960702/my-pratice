# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 11:06:28 2020

@author: zh
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s)-1
        k = 0
        if(len(s)==0):
            return 0
        
        while (i>-1):
            if(s[i]!=' '):
                k+=1
            if(s[i]==' 'and k!=0):
                break
            i-=1
        return k
print (Solution().lengthOfLastWord("aaa"))
                