from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for string in strs:
            alphabet = [0 for _ in range(26)]
            for char in string:
                alphabet[ord(char) - ord("a")] += 1
            seen[tuple(alphabet)].append(string)
        return list(seen.values())
