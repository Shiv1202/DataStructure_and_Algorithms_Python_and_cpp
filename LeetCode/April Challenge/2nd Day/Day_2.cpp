class Solution {
public:
    bool isHappy(int n) 
    {
        set<int> st;
        while(1)
        {
            n=sqsum(n);
            if(n==1)
                return true;
            if(st.find(n)!=st.end())
                return false;
            st.insert(n);
        }
    }
    int sqsum(int n)
    {
        int s=0;
        while(n)
        {
            s+=(n%10)*(n%10);
            n/=10;
        }
        return s;
    }
};
