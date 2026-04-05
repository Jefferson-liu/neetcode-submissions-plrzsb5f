class Solution:
    def dailyTemperatures(self, temperatures):
        ans = [0] * len(temperatures)
        stack = []  # stores indices of unresolved days
        
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prev = stack.pop()
                ans[prev] = i - prev  # resolve the previous day
            stack.append(i)
        
        return ans






