class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        unordered_map<int, int> m;
        m[0]=-1;
        int ans=0, curr=0;
        for(int i=0;i<nums.size();i++)
        {
            curr=curr+ (nums[i]==0? -1:1);
            if(m.count(curr))
                ans= max(ans, i-m[curr]);
            else
                m[curr]=i;
        }
        return ans;
    }
};
