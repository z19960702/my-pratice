from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        used = [False for i in range(len(candidates))]
        candidates.sort()

        def dfs(candidates,path,size,step):
            print (path,step)
            if sum(path)>target:
                return 
            if sum(path)==target:
                res.append(path[:])
                return 
            for i in range(step,len(candidates)):
                if not used[i]:
                    if i > 0 and candidates[i] == candidates[i - 1] and not used[i - 1]:
                        continue
                    used[i] = True
                    path.append(candidates[i])
                    step = i+1
                    dfs(candidates,path,size+1,step)
                    used[i] = False
                    path.pop()

        dfs(candidates,[],0,0)
        return res
print (Solution().combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8))