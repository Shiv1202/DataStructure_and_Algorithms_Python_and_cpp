class Solution {
public:
    static bool comparator(vector<int>& a, vector<int>& b)
    {
        return (a[1]-a[0])>(b[1]-b[0]);
    }
    int twoCitySchedCost(vector<vector<int>>& costs) {
        int n=costs.size();
        sort(costs.begin(),costs.end(),comparator);
        
        int sum=0;
        for(int i=0;i<n;i++)
        {
            sum+= i>=n/2 ? costs[i][1] : costs[i][0];
        }
        return sum;
    }
};
