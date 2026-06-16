class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_hash = dict()

        for i in range(len(nums)):
            if nums[i] in seen_hash:
                arr = []
                arr = [seen_hash[nums[i]], i]
                return arr
            
            seen_hash[target - nums[i]] = i
        return
