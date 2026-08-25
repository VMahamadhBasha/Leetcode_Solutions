class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        setnums=set(nums)
        multiple=k
        while multiple in setnums:
            multiple +=k
        return multiple
        