class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int,int> prevSum;
        int res=0;
        int currsum=0;
        
        for(int i=0;i<nums.size();i++)
        {
            currsum+=nums[i];
            if(currsum==k)
                res++;
            if(prevSum.find(currsum-k) != prevSum.end())
                res+=(prevSum[currsum-k]);
            prevSum[currsum]++;
        }
        return res;
    }
};
