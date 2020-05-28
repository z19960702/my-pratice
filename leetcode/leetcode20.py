# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 21:21:52 2020

@author: zh
"""

class Solution:
    def isValid(self, s: str) -> bool:
        a =[]
        if (s==''):
            return True
        if(len(s)%2==1):
            return False
        for i in s:
            if i=='(' or i=='[' or i=='{':
                a.append(i)
            
            if i==')':
                if (len(a)==0):
                    return False
                t = a.pop(len(a)-1)
                if t !='(':
                    return False
            if i==']':
                if (len(a)==0):
                    return False
                t = a.pop(len(a)-1)
                if t !='[':
                    return False    
            if i=='}':
                if (len(a)==0):
                    return False
                t = a.pop(len(a)-1)
                if t !='{':
                    return False
        if (len(a)==0):
            return True
        else : 
            return False
print (Solution().isValid("())("))