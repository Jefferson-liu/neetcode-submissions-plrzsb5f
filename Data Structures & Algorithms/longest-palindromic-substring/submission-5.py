from collections import deque
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # queue where the first one is the same as the last one
        if len(s) <= 1:
            return s
        
        # start from middle to find palindrome

        def palindrome(i):
            # finds longest palindrome from index i
            inds = (i, i)
            ods = (i, i)
            curMax = 0
            l = i
            r = i
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                inds = (l, r)
                l -= 1
                r += 1
                
            print(inds)
                    
            
            
            if i + 1 < len(s):
                l = i
                r = i + 1 # even length
                while l >= 0 and r < len(s):
                    if s[l] != s[r]:
                        break
                    ods = (l, r)
                    l -= 1
                    r += 1
                print(ods)
                
            if inds[1] - inds[0] < ods[1] - ods[0]:
                inds = ods
            return inds

        curMax = 0
        inds = (0,0)
        for i in range(len(s)):
            l,r = palindrome(i)
            if curMax < r - l:
                inds = (l, r)
                curMax = r - l
        print(inds)
        return s[inds[0]:inds[1] + 1]