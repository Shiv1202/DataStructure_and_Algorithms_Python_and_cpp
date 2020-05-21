class Solution {

public:
        Solution()
        {
            ios::sync_with_stdio(false); 
            std::cin.tie(nullptr); 
            std::cout.tie(nullptr);
        }
    bool canJump(vector<int>& nums) {
        int maxjump=0;
        for(int i=0;i<nums.size();i++)
        {
            if(i>maxjump)
                return false;
            maxjump=max(i+nums[i], maxjump);
        }
        return true; 
    }
};
