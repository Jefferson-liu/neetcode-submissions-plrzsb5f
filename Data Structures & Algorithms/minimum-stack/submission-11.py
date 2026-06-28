
class MinStack:

    def __init__(self):
        self.stack = []
        self.minInd = None
        self.minDict = {} # dict of the index of the next min value


    def push(self, val: int) -> None:
        
        if len(self.stack) == 0:
            self.minInd = 0
            self.minDict[0] = 0
        else:
            if self.stack[self.minInd] > val:
                self.minDict[len(self.stack)] = self.minInd
                self.minInd = len(self.stack)
        self.stack.append(val)
        
    def pop(self) -> None:
        if self.minInd == len(self.stack) - 1:
            self.minInd = self.minDict[self.minInd]
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack[self.minInd]
