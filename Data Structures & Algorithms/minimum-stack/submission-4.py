class MinStack:

    def __init__(self):
        self.stack = []
        self.count = 0
        self.miniStack = []
        self.mini = float('inf')
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.count += 1
        if self.miniStack:
            self.mini = min(self.miniStack[-1], val)
        else:
            self.mini = val
        self.miniStack.append(self.mini)


    def pop(self) -> None:
        self.count -= 1
        self.stack.pop()
        self.miniStack.pop()
        
    def top(self) -> int:
        return self.stack[self.count-1]

    def getMin(self) -> int:
        return self.miniStack[self.count-1]
