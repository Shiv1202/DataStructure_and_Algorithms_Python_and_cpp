class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int,int> mp;
        for(auto i: nums)
            mp[i]++;
        
        for(auto i: mp)
            if(i.second > nums.size()/2)
                return i.first;
        
        return 0;
    }
};
