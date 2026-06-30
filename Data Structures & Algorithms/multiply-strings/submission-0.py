class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # long division
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        ans = []
        long = num1[::-1]
        short = num2[::-1]

        for i in range(len(short)):
            temp = 0
            for j in range(len(long)):
                temp += int(short[i]) * int(long[j]) * (10 ** (i + j)) 
            ans.append(temp)

        return str(sum(ans))