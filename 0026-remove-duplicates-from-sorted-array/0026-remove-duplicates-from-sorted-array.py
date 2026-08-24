class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        st=[]
        if len(nums)==1:
            return 1
        for i in range(len(nums)):
            if not st:
                st.append(i)
            if nums[i]!=nums[st[-1]]:
                st.append(i)
        j=0
        print(st)
        for i in range(len(st)):
            nums[j]=nums[st[i]]
            j+=1
        return j
