class Solution {
public:
    int firstUniqChar(string s) {
        unordered_map<int,int> mp;
        
        for(auto i: s)
            mp[i-'a']++;
        
        for(int i=0;i<s.size();i++)
            if(mp[s[i]-'a']==1)
                return i;
        
        return -1;
    }
};

