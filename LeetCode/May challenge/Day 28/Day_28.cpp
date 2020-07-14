class Solution {
public:
    vector<int> countBits(int num) {
        vector<int> res;
        for(int i=0;i<=num;i++)
        {
            bitset<64> temp(i);// bitset converts the int to its binary 
            res.push_back(temp.count());//count in bitset ciunts the no. of set bits
        }
        return res;
    }
};
