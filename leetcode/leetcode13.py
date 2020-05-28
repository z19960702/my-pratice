# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 22:01:54 2020

@author: zh
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        i = len(s)-1
        sum = 0
        while(i>-1):
            if(i>0 and s[i-1]=='I'and s[i] =='V'  ):
                sum = sum +4
                i-=2
            elif(i>0 and s[i-1]=='I'and s[i] =='X' ):
                sum = sum +9
                i-=2
            elif(i>0 and s[i-1]=='X'and s[i] =='L' ):
                sum = sum +40
                i-=2
            elif(i>0 and s[i-1]=='X'and s[i] =='C' ):
                sum = sum +90
                i-=2
            elif(i>0 and s[i-1]=='C'and s[i] =='D' ):
                sum = sum +400
                i-=2
            elif(i>0 and s[i-1]=='C'and s[i] =='M' ):
                sum = sum +900
                i-=2
            elif(s[i]=='M'):
                sum = sum +1000
                i-=1
            
            elif(s[i]=='D'):
                sum = sum +500
                i-=1
            elif(s[i]=='C'):
                sum = sum +100
                i-=1
            elif(s[i]=='L'):
                sum = sum +50
                i-=1
            elif(s[i]=='X'):
                sum = sum +10
                i-=1
            elif(s[i]=='V'):
                sum = sum +5
                i-=1
            elif(s[i]=='I'):
                sum = sum +1
                i-=1
            
        return sum
print (Solution().romanToInt("MCMXCIV"))