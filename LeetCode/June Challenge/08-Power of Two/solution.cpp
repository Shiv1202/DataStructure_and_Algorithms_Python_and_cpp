class Solution {
public:
    bool isPowerOfTwo(int n) {
        if(n<=0)
            return false;  
        if(log2(n)==int(log2(n)))
            return true;
        else
            return false;
    }
};

