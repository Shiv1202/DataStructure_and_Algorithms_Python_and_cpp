class Solution {
public:
    
    void helper(int i,int j,vector<vector<char>>& grid)
    {
        if(i < 0 || j < 0 || i >= grid.size() || j >= grid[i].size() || grid[i][j] != '1')
            return;
        grid[i][j]=0;
        helper(i+1,j,grid);
        helper(i-1,j,grid);
        helper(i,j+1,grid);
        helper(i,j-1,grid);
    }
    int numIslands(vector<vector<char>>& grid) {
        int island=0;
        for(int i=0;i<grid.size();i++)
        {
            for(int j=0;j<grid[i].size();j++)
            {
                if(grid[i][j]=='1')
                    island++;
                    helper(i,j,grid);
            }
        }
        return island;
    }
};
