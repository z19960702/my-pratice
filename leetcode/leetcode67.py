# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 11:47:00 2020

@author: zh
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if (len(a) < len(b)):
            a = "0"*( len(b)-len(a))+a
        if (len(b) < len(a)):
            b = "0"*( len(a)-len(b))+b    
        l = len(a)
        s = ""
        k = 0
        for i in range(0,l) :
            temp = int(a[len(a)-i-1])+int(b[len(b)-i-1])+k
            k = 0
            if (temp == 0 or temp == 1):
                s = str(temp) +s
            if (temp == 2 ):
                s = str(0)+s
                k = 1
            if(temp == 3 ):
                s = str(1)+s
                k = 1 
            if (i == l-1 and k ==1):
                s ="1"+s    
            print (s)
        return s
print (Solution().addBinary("0", "0"))
                
            