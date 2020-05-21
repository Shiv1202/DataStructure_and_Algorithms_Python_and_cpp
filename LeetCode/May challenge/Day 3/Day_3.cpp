class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        unordered_map<char,int> temp;
        
        for(auto i : ransomNote)
            temp[i]++;
        
        for(auto t: temp)
            if(count(magazine.begin(),magazine.end(),t.first)<t.second)
                return false;
        
        return true;
    }
};
