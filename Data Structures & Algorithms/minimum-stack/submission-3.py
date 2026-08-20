class MinStack:

    def __init__(self):
        self.arr = []
        self.mini = []


    def push(self, val: int) -> None: 
        if not self.arr:
            self.arr.append(val)
            self.mini.append(val)
        else:
            self.mini.append(min(val, self.mini[-1]))
            self.arr.append(val)
    def pop(self) -> None:
        self.arr.pop()
        self.mini.pop()

    def top(self) -> int:
        if self.arr != []:
            return self.arr[-1] 

    def getMin(self) -> int:
        if self.mini:
            return self.mini[-1]