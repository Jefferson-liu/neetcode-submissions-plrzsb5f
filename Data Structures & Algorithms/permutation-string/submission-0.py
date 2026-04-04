class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        n = len(s1)
        m = len(s2)
        sdict = defaultdict(int)
        for char in s1:
            sdict[char] += 1

        for i in range(m-n+1):
            temp = defaultdict(int)
            for char in s2[i: i + n]:
                temp[char] += 1
            isValid = True
            for key in temp:
                if temp[key] != sdict[key]:
                    isValid = False
            if isValid:
                return True
        
        return False