class Solution:

    def encode(self, strs: List[str]) -> str:
        lens = [str(len(s)) for s in strs]
        if lens:
            return " ".join(lens) + "|" + "".join(strs)
        return ""

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        ind = s.index("|")
        lens = s[:ind].split()
        rest = s[ind + 1:]
        ans = []
        cur = 0
        for l in lens:
            ans.append(rest[cur:cur + int(l)])
            cur += int(l)
        return ans
