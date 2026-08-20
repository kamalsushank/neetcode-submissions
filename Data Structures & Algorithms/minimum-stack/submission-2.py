class MinStack:

    def __init__(self):
        self.arr = []
        self.mini = float('inf')

    def push(self, val: int) -> None:
        self.arr.append(val)
        self.mini = min(self.mini , val)        

    def pop(self) -> None:
        val = self.arr.pop()
        if self.mini == val:
            if not self.arr:
                self.mini = float('inf')
            else:
                self.mini = min(self.arr)

    def top(self) -> int:
        if self.arr != []:
            return self.arr[-1] 

    def getMin(self) -> int:
        return self.mini