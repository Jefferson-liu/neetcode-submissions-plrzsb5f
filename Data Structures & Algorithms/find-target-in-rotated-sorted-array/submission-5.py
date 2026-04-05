class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # close to bin search, except there are 2 sorted arrays we want to find the pivot point and do regular binary search from there

        # we know nums[left], we know nums[right], check if nums[mid] < target < nums[right]

        left = 0 
        right = len(nums) - 1

        while left <= right:
            
            mid = (left + right) // 2
            print(mid)
            if left > len(nums) - 1:
                return -1
            if nums[left] == target:
                return left
            elif nums[right] == target:
                return right
            elif nums[mid] == target:
                return mid

            print(left)
            if nums[left] > target:
                if nums[mid] > target: 
                    
                    if nums[right] < nums[mid]:
                        #top half
                        left = mid + 1
                    else:
                        #bot half
                        right = mid - 1
                elif nums[mid] < target:
                    #its top half
                    left = mid + 1

            elif nums[left] < target:
                if nums[mid] < target:
                    #top half
                    left = mid + 1
                elif nums[mid] > target:
                    #bottom half
                    right = mid - 1

            elif nums[right] > target:
                if nums[mid] < target:
                    #top half
                    left = mid + 1
                elif nums[mid] > target:
                    #bottom half
                    right = mid - 1

            elif nums[right] < target:
                if nums[mid] > target:
                    # we know its top half
                    left = mid + 1
                elif nums[mid] < target:
                    #we konw its bottom half
                    right = mid - 1

            # is it possible that nums[right] < target and nums[mid] < target? [3,1,2]
            
            
        return -1 

