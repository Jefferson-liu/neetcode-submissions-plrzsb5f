class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # dfs 
        n = len(nums)
        ans = []
        def dfs(arr, index):
            # array is the array we are using
            if index == n:
                return arr
            
            arr.append(nums[index])
            ans.append(dfs(arr[::], index + 1))
            arr.pop(-1)
            ans.append(dfs(arr[::], index + 1))
            

        dfs([], 0)
        #print(ans)
        return [x for x in ans if x is not None]
                
                