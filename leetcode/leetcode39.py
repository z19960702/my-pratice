from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def dfs(candidates,path):
            if sum(path)>target:
                return 
            if sum(path)==target:
                res.append(path[:])
            for i in range(len(candidates)):
                path.append(candidates[i])
                dfs(candidates[i:],path)
                path.remove(candidates[i])
        dfs(candidates,[])
        return res
print (Solution().combinationSum(candidates = [2,3,5], target = 8))

