class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> seenHash;

        for (int i = 0; i < nums.size(); i++) {
            if (seenHash.find(nums[i]) != seenHash.end()) {
                return {seenHash[nums[i]], i};
            }

            seenHash[target - nums[i]] = i;
        }

        return {};
    }
};
