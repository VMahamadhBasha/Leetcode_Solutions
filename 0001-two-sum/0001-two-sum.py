class Solution:
    def twoSum(self, nums: List[int], t: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==t:
                    return [i,j]

       

        