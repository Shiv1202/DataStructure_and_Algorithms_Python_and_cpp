class Solution {
public:
    void helper(vector<vector<int>>& image, int i, int j, int newColor,int prev)
    {
        if(i < 0 || j < 0 || i >= image.size() || j >= image[i].size() || image[i][j] != prev)
            return;
        image[i][j]=newColor;
        helper(image, i-1, j, newColor, prev);
        helper(image, i+1, j, newColor, prev);
        helper(image, i, j-1, newColor, prev);
        helper(image, i, j+1, newColor, prev);
    }
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int newColor) {
        
        int prev=image[sr][sc];
        if(prev!=newColor)
            helper(image, sr, sc, newColor, prev);
        
        return image;
    }
};
