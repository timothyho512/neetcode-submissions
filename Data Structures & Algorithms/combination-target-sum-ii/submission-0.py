class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # first need to think what is the difference between this and the last question (CombinationSum)

        # first, last question, the array is distinct value while this contains duplicate

        # second, last question, element could be chosen infinitely, while this only once

        # one flag, because this arr contain duplicate, so even if we do the subnet style of pick and skip
        # there could still be a duplicate, so we need something, possibly a hash, to exclude duplicate combinations

        # we have faced this kind of issue before i am pretty sure, but i forgot what kind of data structure
        # we have used for this

        # one thing I have in my mind right now is just hashmap and tuple as key maybe?
        # we also need to find a way to be able to compare the dup as they might have different position order

        res = []
        path = []
        self.total = 0
        candidates.sort()

        def backtrack(i):
            if self.total == target:
                res.append(path[:])
                return
            if self.total > target:
                return
            if i >= len(candidates):
                return
            path.append(candidates[i])
            self.total += candidates[i]
            backtrack(i+1)
            path.pop()
            while i + 1 < len(candidates) and candidates[i+1] == candidates[i]:
                i += 1
            self.total -= candidates[i]
            backtrack(i+1)


        backtrack(0)
        return res