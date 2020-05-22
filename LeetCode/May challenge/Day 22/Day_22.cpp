class Solution {
public:
    string frequencySort(string s) {
        map<char, int> mp;
        for(auto i: s)
            mp[i]++;
        
        priority_queue<pair<int,char>> pq;
        for(auto t: mp)
            pq.push(make_pair(t.second,t.first));
        
        string res;
        while(!pq.empty())
        {   
            int count=pq.top().first;
            while(count)
            {
                res.push_back(pq.top().second);
                count--;
            }
            pq.pop();
        }
        return res;
    }
};
