class Solution {
public:
    int maxSum(vector<int> &num)
    {
        int maxVal=num[0];
        int currMax=num[0];
        
        for(int i=1;i<num.size();i++)
        {
            currMax=max(num[i], currMax+num[i]);
            maxVal=max(maxVal,currMax);
        }
        return maxVal;
    }
    int maxSubarraySumCircular(vector<int>& A) {
        
        int sum1= maxSum(A);
        int totalsum=accumulate(A.begin(),A.end(),0);
        
        transform(A.begin(), A.end(), A.begin(), bind(multiplies<int>(),placeholders::_1, -1));
        
        int sum2=maxSum(A);
        
        if(sum2+totalsum > sum1 && sum2+totalsum !=0)
            return sum2+totalsum;
        else
            return sum1;
        
    }
};
