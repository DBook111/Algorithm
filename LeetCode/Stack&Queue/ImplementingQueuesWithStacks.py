class MyQueue:
    """
    思路：每次有新元素要入队，就利用第二个栈吧所有元素都弹出来，放入新元素，再弹回去
    """
    def __init__(self):        
        self.stack1 = []
        self.stack2 = []
    
    def push(self, x: int) -> None:
        if self.stack1 is None:
            self.stack1.append(x)
            return
        while self.stack1:
            temp = self.stack1.pop()
            self.stack2.append(temp)
        self.stack1.append(x)
        while self.stack2:
            temp = self.stack2.pop()
            self.stack1.append(temp)
    
    def pop(self) -> int:
        if self.stack1 is not None:
            return self.stack1.pop()
    
    def peek(self) -> int:
        return self.stack1[-1]
    
    def empty(self) -> bool:
        if len(self.stack1) > 0:
            return False
        return True