class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # iterate through numbers until we hit an operand - once we hit that, perform operation on number, store running answer, then keep iterating
        stack = []
        for token in tokens:
            if token == "+":
                cur = stack.pop()
                prev = stack.pop()
                stack.append(int(cur) + int(prev))
            elif token == "-":
                cur = stack.pop()
                prev = stack.pop()
                stack.append(int(prev) - int(cur))
            elif token == "*":
                cur = stack.pop()
                prev = stack.pop()
                stack.append(int(cur) * int(prev))
            elif token == "/":
                cur = stack.pop()
                prev = stack.pop()
                stack.append(int(prev / cur))
            else:
                stack.append(int(token))
        return stack[0]

