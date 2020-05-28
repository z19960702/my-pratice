
#使用正则表达式
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        p=''.join(re.findall(r'[\w\d]+',s))
        p=p.lower()
        return True if p==p[::-1] else False


print (Solution().isPalindrome("race a car"))           
