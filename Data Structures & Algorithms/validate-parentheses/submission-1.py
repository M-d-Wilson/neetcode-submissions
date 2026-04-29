class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []
        for c in s:
            if c in ['(', '{', '[']:
                brackets.append(c)
            elif c in [')', '}', ']'] and len(brackets) == 0:
                return False
            elif c == '}' and brackets[-1] == '{':
                brackets.pop()
            elif c == ']' and brackets[-1] == '[':
                brackets.pop()
            elif c == ')' and brackets[-1] == '(':
                brackets.pop()
            else:
                return False
        if len(brackets) > 0:
            return False
        return True
        