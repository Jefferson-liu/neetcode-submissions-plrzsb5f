class Solution:
    def isValid(self, s: str) -> bool:
        # stack : when we see an opening, push onto stack, if we see a closing, if the top of the stack matches the corresponding closing bracket, we pop, if not, return False
        stack = []
        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                if stack:
                    top = stack.pop()
                    if char == ")":
                        if top != "(":
                            return False
                    elif char == "}":
                        if top != "{":
                            return False
                    elif char == "]":
                        if top != "[":
                            return False
                else:
                    return False
            
        return len(stack) == 0


