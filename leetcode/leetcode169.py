from typing import List 
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        length = len (nums)
        temp = nums[0]
        count = 1
        for i in range (1,length):
            if (count == 0 ):
                temp = nums[i]
                count = 1
                continue
            if (temp!=nums[i]):
                count -= 1
            else:
                count +=1
            
        return temp
print (Solution().majorityElement([2]))