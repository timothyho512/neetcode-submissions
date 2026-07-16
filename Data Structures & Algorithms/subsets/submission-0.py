class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # interesting

        # because just looking at the question, i would not think about backtracking
        # or recursion right,
        # maybe a few months ago when i was studying the algorithm course and being very sharp 
        # on which question is which type, maybe I will, but not now

        # so basically,

        # i have a ans arr
        # and everytime, i need to append sth to the array

        # and have a loop that start at one
        self.ans = [[]]

        def dfs(n, current):
            for j in range(n, len(nums)):
                current.append(nums[j])
                self.ans.append(current[:])
                dfs(j+1, current)
                current.pop()

        dfs(0, [])
        return self.ans
        