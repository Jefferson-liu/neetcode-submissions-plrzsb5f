class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.minVal = math.inf

    def push(self, val: int) -> None:
        if val < self.minVal:
            self.minVal = val
        self.minStack.append(self.minVal)
        self.stack.append(val)



    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        if self.minStack:
            self.minVal = self.minStack[-1]
        else:
            self.minVal = math.inf
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        #print(self.minStack)
        #print(self.stack)
        return self.minStack[-1]
        
