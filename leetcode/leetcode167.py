from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
        i = 0
        j = length-1
        num =[]
        if (length)<2:
           return num 
        while i<j:
            if (numbers[i]+numbers[j]<target):
                i+=1
            elif numbers[i]+numbers[j]>target:
                j-=1
            else:
                num = [i+1,j+1]
                break;
        return num

print (Solution().twoSum([ 1],18))



