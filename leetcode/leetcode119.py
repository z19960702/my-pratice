# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 18:57:30 2020

@author: zh
"""
from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [None for _ in range(rowIndex+1)]
        for i in range (1,rowIndex+2):    
            if(i == 1):
                row[0] = 1
            else :
                row[i-1] = 1
                for j in  range(i-1,1,-1):
                    row[j-1] = row[j-1] + row[j-2]     
        return row
print (Solution().getRow(1))
    
