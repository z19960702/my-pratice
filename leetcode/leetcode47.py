from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans= []
        def dfs(paras,temp):   
            if len(paras)==0:
                temp.sort()
                print (temp)
                if (temp not in ans):
                    ans.append(temp[:])
                return 
            for i in range(len(paras)):
                temp.append(paras[i])
                paras.remove(paras[i])
                dfs(paras,temp)
                t = temp.pop()
                paras.insert(i,t)
        dfs(nums,[])
        return ans
print (Solution().permuteUnique([1,1,2]))