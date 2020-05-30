class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int K) {
        multimap< float, vector<int> > dist;
        vector<vector<int>> res;
        for(auto i: points)
        {
            float temp= sqrt(i[0]*i[0]+ i[1]*i[1]);
            dist.insert(make_pair(temp,i));
        }
        
        auto it=dist.begin();
        while(K--)
        {
            res.push_back(it->second);
            it++;
        }
        return res;
    }
};
