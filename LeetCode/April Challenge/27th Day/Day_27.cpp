class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        int m=matrix.size();
        if(m==0)
            return 0;
        int n=matrix[0].size();        
        int sq[m+1][n+1];
        int res=0;
        for(int i=0;i<=m;i++)
        {
            for(int j=0; j<=n;j++)
            {
                if(i==0 || j==0 || matrix[i-1][j-1]=='0')
                    sq[i][j]=0;
                else
                    sq[i][j]=1+ min(sq[i-1][j-1], min( sq[i-1][j], sq[i][j-1]));
                
                res=max(res, sq[i][j]);
            }
        }
        return res*res;      
    }
};
