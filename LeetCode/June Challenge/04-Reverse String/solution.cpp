class Solution {
public:
    void reverseString(vector<char>& s) {
        if(!s.size())
            return;
        for(int i=0,j=s.size()-1;i<=s.size()/2 && j>=s.size()/2;i++,j--)
            swap(s[i],s[j]);
    }
};
