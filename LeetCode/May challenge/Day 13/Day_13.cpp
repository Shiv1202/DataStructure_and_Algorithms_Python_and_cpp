class Solution {
public:
    string removeKdigits(string num, int k) {
        if(num.length()<= k)
            return "0";
        string res;
        for(auto i: num){
            while(k && res.length() && res.back()>i)
            {
                res.pop_back();
                k--;
            }
            res.push_back(i);
        }
        res.resize(res.length()-k);
        int beg=0;
        while(beg< res.length()-1 && res[beg]== '0')
            beg++;
        
        return res.substr(beg, res.length() - beg + 1);
    }
};
