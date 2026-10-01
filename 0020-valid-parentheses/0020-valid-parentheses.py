class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {')' : '(', '}' : '{', ']' : '['}
        if len(s) == 1:
            return False
        for ch in s:
            if ch in d:
                if not stack or stack.pop() != d[ch]:
                    return False
            else:
                stack.append(ch)
        return not stack