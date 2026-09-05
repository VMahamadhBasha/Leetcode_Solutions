class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        m=0
        sm=[0]*len(nums)
        r=len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if nums[i]<=nums[r]:
                sm[i]=nums[i]
                r=i
            else:
                sm[i]=nums[r]   
        for i in range(len(nums)):
            if nums[i]>=nums[m]:
                m=i
            if nums[m]-sm[i]<=k:
                return i
        return -1

        
        