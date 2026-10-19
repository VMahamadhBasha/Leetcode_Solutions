class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        res=[]
        i=0
        while i<len(nums) and nums[i]<=target:
            if nums[i]==target:
                res.append(i)
            i+=1
        return res