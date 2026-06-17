class MinStack:

    def __init__(self):
        self.stack = []
        self.miniStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.miniStack:
            num = min(self.miniStack[-1], val)
        else:
            num = val
        self.miniStack.append(num)


    def pop(self) -> None:
        self.stack.pop()
        self.miniStack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.miniStack[-1]
