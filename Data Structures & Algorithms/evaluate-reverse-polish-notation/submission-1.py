class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for i in tokens:
            if i in  "/*-+" :
                val1 = int(stk.pop())
                val2 = int(stk.pop())
                if i =='+' :
                    v = val1 + val2
                    stk.append(str(v))
                elif i =='-' :
                    v = val2 - val1
                    stk.append(str(v))
                elif i =='*' :
                    v = val1 * val2
                    stk.append(str(v))
                else:
                    v = int(val2 / val1)
                    stk.append(str(v))
            else:
                stk.append(i)
        return int(stk.pop())