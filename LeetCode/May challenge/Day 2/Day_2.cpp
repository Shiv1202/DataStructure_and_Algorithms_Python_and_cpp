class Solution {
public:
    int numJewelsInStones(string J, string S) {
        int sum=0;
        for(auto i : J)
            sum+=count(S.begin(), S.end(), i);
        return sum;
    }
};
