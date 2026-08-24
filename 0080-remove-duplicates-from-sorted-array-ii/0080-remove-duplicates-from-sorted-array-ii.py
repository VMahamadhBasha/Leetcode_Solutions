class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d={}
        st=[]
        for i in range(len(nums)):
            if nums[i] in d:
                if d[nums[i]]<2:
                    st.append(i)
                    d[nums[i]]+=1
            else:
                d[nums[i]]=1
                st.append(i)
        j=0
        for i in range(len(st)):
            nums[j],nums[st[i]]=nums[st[i]],nums[j]
            j+=1
        return j


        