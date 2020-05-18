class Solution {
public:
    int maxProfit(vector<int>& p) {
        vector<int> a(p), b(p);
        sort(a.begin(), a.end(), greater<int>()); 
        sort(b.begin(),b.end());
        
        if(a==p)//check reverse sorted
            return 0;
        
        if(b==p)// check sorted
            return (b[b.size()-1]-b[0]);

        int profit=0;
        for(int i=0;i<(p.size()-1);i++)
        {
            if(p[i+1]>p[i])
                profit=profit+p[i+1]-p[i];
        }
        return profit;
    }
};
