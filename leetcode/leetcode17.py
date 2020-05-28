from typing import List
import itertools
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        maps = {'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        if (len(digits) == 0):
            return []
        if (len(digits) == 1):
            return maps[digits[0]]
        a = maps[digits[0]]
        for i in range(len(digits)-1):
            res = []
            for x in  itertools.product(a,maps[digits[i+1]]):
                s = ""
                s = s+x[0]+x[1]
                res.append(s)
            a = res
            
        return  res
print (Solution().letterCombinations(""))
