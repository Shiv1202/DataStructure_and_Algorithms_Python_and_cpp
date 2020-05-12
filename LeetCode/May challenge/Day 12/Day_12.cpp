class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        set<int> s;
        
        for(auto i: nums)
            s.insert(i);
        
        return (2*accumulate(s.begin(), s.end(), 0)-accumulate(nums.begin(), nums.end(), 0));
    }
};
