class Solution:

    def encode(self, strs: List[str]) -> str:
        payload = ""
        for string in strs:
            payload+=str(len(string)) + " "
        
        payload+="," + ''.join(strs)
        #print(payload)
        return payload


    def decode(self, s: str) -> List[str]:
        commaIndex = -1
        for i, char in enumerate(s):
            if char == ",":
                commaIndex = i
                break
        
        lengths = s[:commaIndex].split()
        strings = s[commaIndex + 1:]

        result = []
        cur = 0
        for length in lengths:
            result.append(strings[cur:cur+int(length)])
            cur+=int(length)
        return result





