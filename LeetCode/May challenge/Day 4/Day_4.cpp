class Solution {
public:
    
    int findComplement(int num) {
        int res=0,p=0;
        while(num)
        {
            res+= !(num%2)*pow(2,p);
            num/=2;
            p++;
        }
        return res;
    }
};
