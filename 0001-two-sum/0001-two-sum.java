class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] res=new int[2];
        Map<Integer,Integer> d=new HashMap<>();
        for(int i=0;i<nums.length;i++){
            int b=target-nums[i];
            if(d.containsKey(b)){
                res[0]=d.get(b);
                res[1]=i;
                return res;
            }
            else{
                d.put(nums[i],i);
            }
        }
        return res;
        
    }
}