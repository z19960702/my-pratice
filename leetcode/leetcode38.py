# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 21:43:21 2020

@author: zh
"""

class Solution:
    def countAndSay(self, n: int) -> str:
        if(n ==1):
            return "1"
        if(n ==2):
            return "11"
        s = "11"
        for i in range(n-2):
            temp = ""
            j = 1
            k = 1
            while(j < len(s)):                  
                if(s[j-1] == s[j]):
                    k+=1        
                else:
                   temp = temp + str(k) + s[j-1]
                   k = 1
                if(j == len(s)-1):      
                    temp = temp + str(k) + s[j]
                    break 
                j+=1
            s = temp
        return s

print (Solution().countAndSay(4))