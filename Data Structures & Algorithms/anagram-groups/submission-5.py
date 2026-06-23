from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        counts = defaultdict(list)
        for s in strs:
            alphabet = [0] * 26
            for char in s:
                alphabet[ord(char) - 97] += 1
            counts[tuple(alphabet)].append(s)
        return list(counts.values())

