class Solution:

    def encode(self, strs: List[str]) -> str:
        #lets record the lengths of each string then
        strLengths = []
        for s in strs:
            strLengths.append(str(len(s)))
        print(strLengths)
        print(' '.join(strLengths) + '|' + ''.join(strs))
        return ' '.join(strLengths) + '|' + ''.join(strs)

    def decode(self, s: str) -> List[str]:
        # we want to find the first index of an |
        ind = 0
        if len(s) == 1:
            return []
        for i in range(len(s)):
            if s[i] == '|':
                ind = i
                break
        nums = [int(i) for i in s[:ind].split(" ")]
        rest = s[ind + 1:]
        cur = 0
        strings = []
        for i in nums:
            strings.append(rest[cur:cur + i])
            cur += i
        print(strings)
        return strings
