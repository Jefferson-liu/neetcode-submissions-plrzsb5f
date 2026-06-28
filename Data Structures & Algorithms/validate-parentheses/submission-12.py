class Solution:
    def isValid(self, s: str) -> bool:
        bmap = {"[":"]", "(":")", "{":"}"}
        stack = []
        if len(s) <= 1:
            return False
        for i in range(len(s)):
            if s[i] in "{([":
                stack.append(s[i])
            elif s[i] in "}])":
                if not stack or bmap[stack[-1]] != s[i]:
                    return False
                else:
                    stack.pop()
        return len(stack) == 0
