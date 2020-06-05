class Solution {
public:
    vector<int> prefix_sum;
    Solution(vector<int>& w) 
    {
        for(auto i: w)
        {
            if(prefix_sum.empty())
                prefix_sum.push_back(i);
            else
                prefix_sum.push_back(i+prefix_sum.back());
        }
    }
    
    int pickIndex() 
    {
        int r= rand() % prefix_sum.back();
        return upper_bound(prefix_sum.begin(),prefix_sum.end(),r) - prefix_sum.begin();
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(w);
 * int param_1 = obj->pickIndex();
 */
