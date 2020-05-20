class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        int m=text1.length()+1;
        int n=text2.length()+1;
        int LCS[m][n];
        for(int i=0;i<m;i++)
        {
            LCS[i][0]=0;
        }
        for(int j=0;j<n;j++)
        {
            LCS[0][j]=0;
        }
        for(int i=1;i<m;i++)
        {
            for(int j=1;j<n;j++)
            {
                if(text1[i-1]==text2[j-1])
                    LCS[i][j]=1+LCS[i-1][j-1];
                else
                    LCS[i][j]=max(LCS[i-1][j], LCS[i][j-1]);
            }
        }
        return LCS[m-1][n-1];
    }
};
