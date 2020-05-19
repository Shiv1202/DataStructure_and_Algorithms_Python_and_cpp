class Solution {
public:
    int countElements(vector<int>& arr)
    {
        int c=0;
        map<int, int> maps;
        for(auto t: arr)
            maps[t]++;
        for(auto i: maps)
            if(maps.find(i.first +1)!=maps.end())
                c+=i.second;
        return c;
    }
};
