class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string> > mymap;
        int n=strs.size();
        string temp;
        
        for(auto i: strs)
        {
            temp=i;
            sort(i.begin(),i.end());
            mymap[i].push_back(temp);
        }
        vector<vector<string>> result;
        
        for(auto t: mymap)
            result.push_back(t.second);
        
        return result;
    }
};
