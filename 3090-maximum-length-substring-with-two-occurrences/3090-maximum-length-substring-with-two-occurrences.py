class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        res=0
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                d=Counter(s[i:j+1])
                b=True
                for k in d.keys():
                    if d[k]>2:
                        b=False
                if b:
                    res=max(res,j-i+1)
        return res
        # l,r=0,0
        # res=0
        # d={}
        # while r<n or l<n:
        #     if s[r] not in d:
        #         d[s[r]]=1
        #     else:
        #         d[s[r]]+=1
        #         if d[s[r]]==2:
        #             res=max(res,r-l)
        #         elif d[s[r]]>2:
        #             l     