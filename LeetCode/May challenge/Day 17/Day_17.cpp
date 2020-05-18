class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        vector<int>  res, hash(26,0), phash(26,0);
        int window=p.size(), len=s.size();
        
        if(len<window)
            return res;
        int left=0, right=0;
        
        while(right<window) // for maintaing freq vector for p and for first window in s
        {
            phash[p[right]-'a']++;
            hash[s[right]-'a']++;
            right++;
        }
        right--;
        while(right<len)
        {
            if(phash==hash)
                res.push_back(left);
            right++;
            if(right!=len)
                hash[s[right]-'a']++;
            
            hash[s[left]-'a']--;
            left++;
        }
        return res;
    }
};
