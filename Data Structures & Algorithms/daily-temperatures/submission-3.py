class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # if they are all decreasing, we can know that there is no day so its 0
        # decreasing stack, loop until it is lesser, that is just O(n^2)
        # cannot sort cause of O(n)
        # either next value is greater, or lesser, if it is lesser, we add this to the stack
        # store the stack in increasing order, min val on top, store index and value. 
        # track current index and value, if the cur value is more than top of the stack value, keep popping and set the index for that to the diff
        ans = [0 for _ in range(len(temperatures))]
        stack = [(0, temperatures[0])]
        for i in range(1, len(temperatures)):
            while stack and temperatures[i] > stack[-1][1]:
                index, temp = stack.pop()
                ans[index] = i - index
            stack.append((i, temperatures[i]))
        return ans