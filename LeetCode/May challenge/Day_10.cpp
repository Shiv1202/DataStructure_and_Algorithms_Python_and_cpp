class Solution {
public:
    int findJudge(int N, vector<vector<int>>& trust) {
        if(N==1)
            return 1;
        vector<int> a, b;
        for(int i=0; i<trust.size(); i++)
        {
            a.push_back(trust[i][0]);
            b.push_back(trust[i][1]);
        }
        for(auto i: b)
        {
            if(find(a.begin(),a.end(),i)==a.end() && count(b.begin(),b.end(),i)==N-1)
                return i;
        }
        return -1;
    }
};
