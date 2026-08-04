class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        res=[]
        s=set(nums)
        nums.sort()
        for i in range(nums[0],nums[-1]):
            if i not in s:
                res.append(i)
        return res        