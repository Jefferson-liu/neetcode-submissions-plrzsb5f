class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # three pointer
        
        sortedNums = sorted(nums)
        triplets = []

        for p1 in range(len(nums) - 2):
            
            if sortedNums[p1] > 0:
                break

            if p1 > 0 and sortedNums[p1] == sortedNums[p1 - 1]:
                continue
                
            p2 = p1 + 1
            p3 = len(sortedNums) - 1
            target = -1 * sortedNums[p1]
            while p2 < p3:
                if sortedNums[p2] + sortedNums[p3] == target:
                    triplets.append([sortedNums[p1], sortedNums[p2], sortedNums[p3]])
                    p2 += 1
                    p3 -= 1
                    while p2 < p3 and sortedNums[p2] == sortedNums[p2 - 1]:
                        p2 += 1
                elif sortedNums[p2] + sortedNums[p3] < target:
                    p2 += 1
                else:
                    p3 -=1
        return triplets
            
            