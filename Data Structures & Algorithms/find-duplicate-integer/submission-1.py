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
        # but this is O(n) space for the seen and O(n) time for looping the for loop


        # the follow up here wants O(1) space and at the same time not modifying the array nums here

        # so I am thinking right now what is the correlation between mentioning O(1) space and not modifying the array
        # so maybe someone can modify an array and use that to indicate something because that does not count as space
        # oh so that one might be, sorting the array and loop through the array and compare nums[i] and nums[i-1]

        # we cant modify the array but O(1) extra space

        # as this problem is from linked list (kind of get hinted)

        # so there has to be something related to linked list

        # maybe turn the array into a linked list, but that is breaking the rule no? both modifying the array or extra space

        # i need to try to think using the info

        # what info we have now

        # this array is n + 1 length

        # and integer could only be [1, n]

        # so there has to be one duplicate at least minimum as shown in the second example

        # or it could be having more as shown in example 1 (missing 4) instead

        slow = nums[0]
        fast = nums[0]

        while true:
            fast = nums[fast]
            fast = nums[fast]
            slow = nums[slow]

            if fast == slow:
                return fast
