class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        a, b = nums1, nums2

        total = len(a) + len(b)
        half = total // 2

        if len(b) < len(a):
            a,b = b,a
        
        # binary search on A
        l,r = 0, len(a) - 1

        while True:
            i = (l + r) // 2 # a
            j = half - i - 2 # b (i + 1 is in i, so its half - (i + 1) and then - 1 as well cause we want to have index for 0 index)
            aleft = a[i] if i >= 0 else -1 * math.inf
            aright = a[i + 1] if i + 1 < len(a) else math.inf
            bleft = b[j] if j >= 0 else -1 * math.inf
            bright = b[j + 1] if j + 1 < len(b) else math.inf
            
            #lpartition is right
            if aleft <= bright and bleft <= aright:
                if total % 2 == 1:
                    # odd
                    return min(aright, bright)
                return (min(aright, bright) + max(aleft, bleft)) / 2
            elif aleft > bright:
                # aleft is too big, reduce size of a
                r = i - 1 # shift
            else:
                # aleft is too small, add left index
                l = i + 1


        
        

