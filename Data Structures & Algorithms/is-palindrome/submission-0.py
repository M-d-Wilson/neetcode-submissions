class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        p1 = ""
        p2 = ""
        p1count = 0
        p2count = len(s) - 1
        while p1count < p2count:
            p1 = s[p1count]
            p2 = s[p2count]
            if not p1.isalnum():
                p1count += 1
                continue
            if not p2.isalnum():
                p2count -= 1
                continue
            if p1 != p2:
                print (p1, ", ", p2)
                return False
            else:
                p1count += 1
                p2count -= 1

            
        return True