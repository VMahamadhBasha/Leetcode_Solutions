class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        st1=[]
        st2=[]
        n=len(nums)
        i=2
        st1.append(nums[0])
        st2.append(nums[1])
        while i<n:
            if st1[-1]>st2[-1]:
                st1.append(nums[i])
            else:
                st2.append(nums[i])
            i+=1
        return st1+st2