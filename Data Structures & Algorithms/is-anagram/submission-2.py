class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = defaultdict(int)
        for char in s:
            dict1[char] += 1
        if len(s) != len(t):
            return False
        for char in t:
            if char in dict1:
                if dict1[char] > 0:
                    dict1[char] -= 1
                else:
                    return False
            else:
                return False
        return True