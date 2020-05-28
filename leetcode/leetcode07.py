# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 20:47:09 2020

@author: zh
"""
from typing import List
class Solution:
    def reverse(self, x: int) -> int:
        '''
        使用字符串来做
        s = str(x)[::-1].rstrip('-')
        if int(s) < 2**31:
            if x >=0:
                return int(s)
            else:
                return 0-int(s)
        return  0
        '''
        
        sum = 0
        a = abs(x)
        k = 0
        while(a):
            print (a)
            k = a%10
            
            sum = sum*10 + k
            a = int(a/10)
            if(sum > pow(2,31)-1):
                sum = 0
                break;
        if(x>=0):
            return sum
        else:
            return -sum
test =  Solution()
print (test.reverse(-1563847412))