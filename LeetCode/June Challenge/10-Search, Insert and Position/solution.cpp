class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {

        return lower_bound (nums.begin(), nums.end(), target)-nums.begin();
    }
};

/*The lower_bound() method in C++ is used to return an iterator pointing to the first element in the range [first, last) which has a 
value not less than val. This means that the function returns the index of the next smallest number just greater than or equal to that
number. If there are multiple values that are equal to val, lower_bound() returns the index of the first such value.*/
