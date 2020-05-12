class Solution {
public:
    int firstBadVersion(int n) {
        long long int low=1, high=n;
        while(low<=high)
        {
            long long int mid=(low+high)/2;
            if(isBadVersion(mid)==true)
                high=mid-1;
            else
                low=mid+1;
        }
        return low;
    }
};
