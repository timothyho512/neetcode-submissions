class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # my understanding the pattern is always the this:
        # two numbers and then there will be one operation
        # i think that is always the case
        ops = set()
        ops.add("+")
        ops.add("-")
        ops.add("*")
        ops.add("/")
        stack = []
        for c in tokens:
            if c not in ops:
                stack.append(int(c))
            else:
                y = stack.pop()
                x = stack.pop()
                if c == "+":
                    result = x + y
                elif c == "-":
                    result = x - y
                elif c == "*":
                    result = x * y
                elif c == "/":
                    # not // because this is round down
                    # but here we jsut dont want the decimal
                    #e.g. -3.33 to -3 and not -4
                    result = int(x / y)
                stack.append(result)
        
        return stack.pop()