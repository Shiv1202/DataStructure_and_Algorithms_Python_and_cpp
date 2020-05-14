class Solution {
public:
    bool checkStraightLine(vector<vector<int>>& coordinates) {
        if(coordinates.size()==2)
            return true;
        
        auto dx=(coordinates[1][0]-coordinates[0][0]);
        auto dy=(coordinates[1][1]-coordinates[0][1]);
        
        for(int i=2;i<coordinates.size();i++)
            if(dy*(coordinates[i][0]-coordinates[i-1][0])!=dx*(coordinates[i][1]-coordinates[i-1][1]))
                return false;
        
        return true;
    }
};
