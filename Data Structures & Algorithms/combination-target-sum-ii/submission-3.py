class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        n = len(candidates)
        def dfs(ind, curSum, comb):
            if ind >= n:
                return
            new = comb.copy()
            new.append(candidates[ind])
            if curSum + candidates[ind] == target:
                ans.append(new)
                return
            if curSum + candidates[ind] < target:
                dfs(ind + 1, curSum + candidates[ind], new)
                new.pop()
            else:
                return
            
            tempInd = ind
            while tempInd < n and candidates[ind] == candidates[tempInd] :
                tempInd += 1

            dfs(tempInd, curSum, new)
        
        dfs(0, 0, [])
        return ans
            