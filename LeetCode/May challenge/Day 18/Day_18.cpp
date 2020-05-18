class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        vector<int> s2hash(26,0), s1hash(26,0);
        int window=s1.size(), len=s2.size();
        
        if(len<window)
            return false;
        int left=0, right=0;
        
        while(right<window) // for maintaing freq vector for s1 and for first window in s2
        {
            s1hash[s1[right]-'a']++;
            s2hash[s2[right]-'a']++;
            right++;
        }
        right--;
        while(right<len)
        {
            if(s1hash==s2hash)
                return true;
            right++;
            if(right!=len)
                s2hash[s2[right]-'a']++;
            
            s2hash[s2[left]-'a']--;
            left++;
        }
        return false;
    }
};
