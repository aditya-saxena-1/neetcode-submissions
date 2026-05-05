class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        int n = size(nums);
        int flag = 0;
        for (int i = 0; i <= n; i++) {
            for (int j = i+1; j <= n; j++) {
                if (nums[i] == nums[j]) {
                    flag = 1;;
                    break;
                }
            }
        }
        if (flag == 1) {
            return true;
        }
        else {
            return false;
        }
    }
};