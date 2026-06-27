class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        counts = [0 for _ in range(26)]
        s1Count = [0 for _ in range(26)]
        for char in s1:
            s1Count[ord(char) - ord("a")] += 1
        for char in s2[:len(s1)]:
            counts[ord(char) - ord("a")] += 1
        if counts == s1Count:
                return True
        for i in range(len(s1), len(s2)):
            counts[ord(s2[i]) - ord("a")] += 1
            counts[ord(s2[i - len(s1)]) - ord("a")] -= 1
            if counts == s1Count:
                return True
        return False
