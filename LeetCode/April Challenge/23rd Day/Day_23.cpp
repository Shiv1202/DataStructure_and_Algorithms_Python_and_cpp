class Solution {
public:
    int rangeBitwiseAnd(int m, int n) {
        if (m==0)
            return 0;
        int a=log2(m);
        int b=log2(n);
        if(a!=b)
            return 0;
        else
        {
            long long int res=m;
            for(long long int i=m;i<=n;i++)
                res&=i;
            return res;
        }
    }
};
