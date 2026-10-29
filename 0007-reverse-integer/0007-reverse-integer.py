class Solution:
    def reverse(self, x: int) -> int:
        s=0
        if x>0:
            s=1
        else:
            s=-1
            x *=-1
        res=0
        while x:
            r=x%10
            res =res*10+r
            x//=10
        return res*s if res<=2**31-1 else 0