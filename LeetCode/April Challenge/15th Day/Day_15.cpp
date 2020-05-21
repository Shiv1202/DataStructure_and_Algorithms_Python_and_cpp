class Solution {
public:
    vector<int> productExceptSelf(vector<int>& v) {
        vector<int> res(v.size());
        int temp=1;
        res[0]=temp;
        for(int i=0;i<v.size()-1;i++)
        {
            res[i+1]=temp*v[i];
            temp=res[i+1];
        }
        temp=1;
        for(int i=v.size()-2;i>=0;i--)
        {
            temp=temp*v[i+1];
            res[i]=res[i]*temp;
            
        }
        return res;
    }
};
