class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r=0,0
        s=0
        res=float('inf')
        while l<=r:
            if s>=target:
                res=min(res,r-l)
                s-=nums[l]
                l+=1
            else:
                if r>=len(nums):
                    return res if res!=float('inf') else 0
                s+=nums[r]
                r+=1
        return res if res!=float('inf') else 0

        

        