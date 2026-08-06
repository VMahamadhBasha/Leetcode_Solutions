class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        res=0
        for i in range(n,n+11):
            k=1
            j=i
            while j>0:
                r=j%10
                k *=r
                j //=10
            if k%t==0:
                return i