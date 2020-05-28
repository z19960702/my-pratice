from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        vol = 0
        while(i<j):
            vol = (j-i)*min(height[i],height[j]) if (j-i)*min(height[i],height[j])> vol else vol
            if (height[i]<=height[j]):
                i+=1
            else:
                j-=1
        return vol
print (Solution().maxArea( [1,8,6,2,5,4,8,12,0]))