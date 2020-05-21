class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
     while(stones.size()>1)
     {
         sort(stones.begin(),stones.end());
         int n=stones.size();
         cout<<n;
         int a=stones[n-1];
         int b=stones[n-2];
         stones.pop_back();
         stones.pop_back();
         if(a!=b)
             stones.push_back(a-b);
     }
        if(stones.size()==0)
            return 0;
        else
            return stones[0];
    }
};
