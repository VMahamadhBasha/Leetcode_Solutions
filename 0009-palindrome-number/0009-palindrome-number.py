class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        res=0
        y=x
        while x:
            r=x%10
            res=res*10+r
            x//=10
        return res==y
