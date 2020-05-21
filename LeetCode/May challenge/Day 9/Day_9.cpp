class Solution {
public:
    bool isPerfectSquare(int num) {
        if(num==0 || num==1)
            return true;
        
        long long int start=2,end=num;
        
        while(start<end)
        {
            long long int mid=(start+end)/2;
            
            if(mid*mid==num)
                return true;
            else
                if(mid*mid<num)
                    start=mid+1;
                else
                    end=mid;
        }
        return false;
    }
};
