class Solution {
public:
    vector<int> prefix_sum;
    Solution(vector<int>& w) 
    {
        for(auto i: w)
        {
            if(prefix_sum.empty())
                prefix_sum.push_back(i);
            else
                prefix_sum.push_back(i+prefix_sum.back());
        }
    }
    
    int pickIndex() 
    {
        int r= rand() % prefix_sum.back();
        return upper_bound(prefix_sum.begin(),prefix_sum.end(),r) - prefix_sum.begin();
        //upper_bound() returns an iterator pointing to the first element in the range [first, last) that is greater than value, or last if no such element is found. 
    }
    //using linear search
    /*
    int pickIndex() 
    {
        int i,r= rand() % prefix_sum.back();
        for(i=0;i<prefix_sum.size();i++)
        {
            if(prefix_sum[i]>r)
                break;
        }
        return i;
    }
    */

    //using binary search
    /*
    int pickIndex() 
    {
        int left = 0, right = accu.size();
        int tgt = rand() % sum;
        while(left < right){
            int mid = left + (right-left) / 2;
            if(accu[mid] <= tgt) left = mid + 1;
            else right = mid;
        }
        return right;
    }
    */
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(w);
 * int param_1 = obj->pickIndex();
 */
