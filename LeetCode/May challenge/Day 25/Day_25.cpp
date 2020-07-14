class Solution {
public:
    int maxUncrossedLines(vector<int>& A, vector<int>& B) {
        if(A.size()==0 || B.size()==0)
            return 0;
        int res=INT_MIN;
        vector<vector<int>> dp(A.size()+1 ,vector<int>(B.size()+1,0));
        
        for(int i=1;i<=A.size();i++)
        {
            for(int j=1;j<=B.size();j++)
            {
                if(A[i-1]==B[j-1])
                    dp[i][j]=dp[i-1][j-1]+1;
                else
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1]);
                res=max(res,dp[i][j]);
            }
        }
        
        return res;
    }
};
