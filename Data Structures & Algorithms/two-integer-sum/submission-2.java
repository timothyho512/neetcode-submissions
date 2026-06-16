class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> seenHash = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            if (seenHash.containsKey(nums[i])) {
                return new int[]{seenHash.get(nums[i]), i};
            }

            seenHash.put(target - nums[i], i);
        }

        return new int[]{};
    }
}
