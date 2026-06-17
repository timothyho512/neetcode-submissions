class Solution:
    def isValid(self, s: str) -> bool:
        dic = {"}":"{", "]":"[", ")":"("}
        stack = []
        for ch in s:
            if ch not in dic:
                stack.append(ch)
            else:
                if not stack:
                    return False

                c = stack.pop()
                if c != dic[ch]:
                    return False
        
        return len(stack) == 0