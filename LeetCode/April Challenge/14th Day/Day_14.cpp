class Solution {
public:
    void leftrotate(string &s, int d) 
    { 
        reverse(s.begin(), s.begin()+d); 
        reverse(s.begin()+d, s.end()); 
        reverse(s.begin(), s.end()); 
    } 
    void rightrotate(string &s, int d) 
    { 
       leftrotate(s, s.length()-d); 
    }
    string stringShift(string s, vector<vector<int>>& shift) {
        
        for(auto i: shift)
        {
            if(i[0]==0)
                leftrotate(s, i[1]);
            else
                rightrotate(s, i[1]);
        }
        return s;
    }
};
