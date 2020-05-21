class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0;
        int r = nums.size() - 1;
        int n = nums.size();
        while(l <= r) {
            int mid = l + (r - l) /2;
            if(nums[mid] == target)return mid;
            if((target<nums[mid] && nums[0] <= target)||(nums[mid]>target && nums[0]>nums[mid])||(nums[0]<=target && nums[mid] < nums[0]))
                r = mid -1;
            else l = mid + 1;
        }
        return -1;
    }
};
