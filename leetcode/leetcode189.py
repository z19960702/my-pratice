from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        
        length = len(nums)
        k = k % length
        current = 0
        moveNum = nums[current]
        temp = 0
        start = 0
        for i in range(length)  :
            current = (current+k) % length
            temp = nums[current]
            nums[current] = moveNum
            moveNum = temp
            if (current == start): 
                current = (current+1)%length
                start = current
                moveNum = nums[current]
            print (nums,moveNum,current)

Solution().rotate([-1,-100,3,99],3)
            