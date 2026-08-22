class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s=0
        p=1
        t=n
        while t>0:
            k=t%10
            s+=k
            p *=k
            t//=10
        if n%(s+p)==0:
            return True
        else:
            return False
        