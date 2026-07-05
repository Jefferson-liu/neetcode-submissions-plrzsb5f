class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # dfs 
        n = len(nums)
        ans = []
        def dfs(arr, index):
            # array is the array we are using
            if index == n:
                ans.append(arr[::])
                return
            
            arr.append(nums[index])
            dfs(arr[::], index + 1)
            arr.pop(-1)
            dfs(arr[::], index + 1)
            

        dfs([], 0)
        return ans
                
                