from typing import List
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        ans = []
        length = len(S)
        def backtrack(s, bit):
            print (s,bit)
            if bit == length:
                ans.append(''.join(s))
                return
            
            if S[bit] <= 'z'and S[bit] >= 'a':
                s.append(S[bit])
                backtrack(s,bit+1 )
                s.pop()
                s.append(S[bit].upper())
                backtrack(s,bit+1 )
                s.pop()
            elif S[bit] <= 'Z'and S[bit] >= 'A':
                s.append(S[bit])
                backtrack(s,bit+1)
                s.pop()
                s.append(S[bit].lower())
                backtrack(s,bit+1 )
                s.pop()
            else:
                s.append(S[bit])
                backtrack(s,bit+1)
                s.pop()
            
        backtrack([], 0)
        return ans
print (Solution().letterCasePermutation(S = "3z4abc"))