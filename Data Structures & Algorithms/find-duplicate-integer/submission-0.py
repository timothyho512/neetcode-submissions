class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # ok first we dont look at the follow up first

        # in the usual case when i looked into this question, i will quickly try to use a set()

        seen = set()

        for n in nums:
            if n in seen:
                return n
            seen.add(n)
        
        # something like that