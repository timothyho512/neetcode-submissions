class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # ok so becasue the same number can be chosen unlimited times
        # this should make the question harder right?

        # would there be like a choice something like for each element
        # choose either pick it or skip it
        # does that make sense here?
        # i think it still make sense, just once you skip it, then it fully skip it
        # but if you pick it, you can pick it again right?

        # so very similar from the Subsets question and the only difference is isndie the loop we dont incrermtn by 1 but just loop through again

        res = []
        path = []
        self.total = 0

        def backtrack(i):
            if self.total == target:
                res.append(path[:])
                return
            if self.total > target:
                return
            if i >= len(nums):
                return
            path.append(nums[i])
            self.total += nums[i]
            backtrack(i)
            path.pop()
            self.total -= nums[i]
            backtrack(i+1)

        backtrack(0)
        return res

