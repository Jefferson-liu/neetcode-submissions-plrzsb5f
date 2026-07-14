class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def dfs(s, opened, closed):
            if len(s) == 2 * n:
                ans.append(s)
                return
            if closed > opened:
                return
            if opened < n:
                # we can open one
                newS = s + "("
                dfs(newS, opened + 1, closed)
            if opened > 0 and closed < opened:
                # we can close one
                newS = s + ")"
                dfs(newS, opened, closed + 1)
        dfs("", 0, 0)
        return ans
