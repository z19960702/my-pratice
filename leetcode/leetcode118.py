# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 17:47:57 2020

@author: zh
"""
from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        tri = []
        for i in range (1,numRows+1):
            row = [None for _ in range(i)]
            if(i == 1):
                row[0] = 1
            else :
                row[0] = 1
                row[i-1] = 1
                for j in  range(1,i-1):
                    row[j] = tri[i-2][j-1] + tri[i-2][j]
            tri.append(row)       
        return tri
print (Solution().generate(1))
                    
                
                
            
                
                