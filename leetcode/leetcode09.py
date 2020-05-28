# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 21:29:30 2020

@author: zh
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = []
        flag = True
        if(x == 0 ):
            return True
        elif(x <0 or x%10==0):
            return False
        
        else : 
            while (x):
                a.append(x%10)
                x = x//10
            for i in range(len(a)//2):
                if(a[i]!=a[len(a)-i-1]):
                    flag = not flag
                    break
                
            if(flag):
                return True
            else:
                return False
            
            
print (Solution().isPalindrome(0))         
        