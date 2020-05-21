class Solution {
public:
    int singleNumber(vector<int>& nums)
    {   int res;
        unordered_map<int, int> freq;
        
        for(int const &i: nums)
            freq[i]++;
        
        for(auto i: freq)
        {
            if(i.second==1)
            {res=i.first;
             break;
            }
            
        }
        return res;
    }
};
