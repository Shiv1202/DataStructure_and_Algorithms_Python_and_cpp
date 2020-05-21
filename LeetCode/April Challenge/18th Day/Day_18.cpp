class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        vector<vector<int>> temp(grid);
        if(temp.size()==0)
            return 0;
        for(int i=0;i<temp.size();i++)
        {
            for(int j=0;j<temp[i].size();j++)
            {
                if(i==0 && j>0)
                    temp[i][j]+=temp[i][j-1];
                else
                {
                    if(j==0 && i>0)
                        temp[i][j]+=temp[i-1][j];
                    else
                        if(i>0 && j>0)
                             temp[i][j]+=min(temp[i-1][j],temp[i][j-1]);
                }
            }
        }
        return temp[temp.size() -1][temp[0].size()-1];
    }
};
