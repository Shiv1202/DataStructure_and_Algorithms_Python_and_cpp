class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int maximum=nums[0], currmax=nums[0];
        for(int i=1;i<nums.size();i++)
        {
            currmax=max(nums[i],currmax+nums[i]);
            maximum=max(maximum,currmax);
        }
        return maximum;
    }
};
