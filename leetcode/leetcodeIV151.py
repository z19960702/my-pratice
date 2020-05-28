class Solution:
    def reverseWords(self, s: str) -> str:
        
        print (s.split()[::-1])
Solution().reverseWords("  hello world!  ")