class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # traverse the array like a linked list with a fast and slow
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
            
        
        slow2 = nums[0]
        while slow2 != slow:
            slow = nums[slow]
            slow2 = nums[slow2]
        return slow
        