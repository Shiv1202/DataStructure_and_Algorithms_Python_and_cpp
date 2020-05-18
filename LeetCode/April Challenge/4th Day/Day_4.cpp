class Solution {
public:
    void moveZeroes(vector<int>& a)
    {
        for(int j=0;j<(count(a.begin(),a.end(),0));j++)
        {    
            for(int i=0;i<(a.size()-1);i++)
                if((a[i]==0)&&(a[i+1]!=0))
                   swap(a[i],a[i+1]);
        }
    }
};
