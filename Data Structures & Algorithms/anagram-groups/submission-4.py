class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        seen = defaultdict(list)
        for string in strs:
            # find number of each char in string, then compare to previous stored valuenumbers
            
            templist = [0] * 26
            for char in string:
                templist[ord(char) - ord('a') ] += 1
            comp = tuple(templist)
            seen[comp].append(string)
        for val in seen.values():
            ans.append(val)
        return ans

