class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # three pointer
        # sort the array first by index
        sortedNums = sorted(nums)
        triplets = set()
        p1 = 0
        
        while p1 < len(nums) - 2 and sortedNums[p1] <= 0:
            target = -1 * sortedNums[p1]
            p2 = p1 + 1
            p3 = len(nums) - 1
            seen = set()
            while p2 < p3:
                if sortedNums[p2] + sortedNums[p3] == target:
                    triplets.add(tuple(x for x in sorted([sortedNums[p1], sortedNums[p2], sortedNums[p3]])))
                    p2 += 1
                elif sortedNums[p2] + sortedNums[p3] < target:
                    p2 += 1
                else:
                    p3 -=1
            p1 += 1
                    
            
                
            
            


        
        return [list(triplet) for triplet in triplets]
            
            