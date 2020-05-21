class Solution {
public:
    int countSquares(vector<vector<int>>& matrix) {
        int sum=0;
        vector<vector<int>> dp( matrix.size()+1 , vector<int> (matrix[0].size()+1, 0));
        
        for(int i=1;i<=matrix.size();i++)
        {
            for(int j=1;j<=matrix[0].size();j++)
            {
                if(matrix[i-1][j-1]!=0)
                    dp[i][j]=min({dp[i-1][j],dp[i][j-1],dp[i-1][j-1]})+1;
                    
                sum+=dp[i][j];
            }
        }
        return sum;
    }
};
