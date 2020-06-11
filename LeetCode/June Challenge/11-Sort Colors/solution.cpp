class Solution {
public:
    void sortColors(vector<int>& nums) {
        if(nums.size()==0 || nums.size()==1)
            return;
        
        int start=0,end=nums.size()-1,index=0;
        
        while(index<=end && start<end)
        {
            if(nums[index]==0)
            {
                swap(nums[index],nums[start]);
                start++;
                index++;
            }
            else if(nums[index]==2)
            {
                swap(nums[index],nums[end]);
                end--;
            }
            else
                index++;
        }
    }
};
