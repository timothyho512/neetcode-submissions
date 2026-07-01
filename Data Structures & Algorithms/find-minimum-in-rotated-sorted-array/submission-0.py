class Solution:
    def findMin(self, nums: List[int]) -> int:
        # so yea O(n) is just scanning the whole array so it is trivial

        # the question required O(logn) so obviously it is binary search

        # and so binary search onl works on sorted array

        # and the array is sorted but it is rotated

        # so the hard part of this question is to how do we actually do binary search on a 
        # rotated sorted array

        # one thing that I have in my mind right now

        # is that when we do binary search

        # we have left and right

        # usually left = 0, right = len(arr) - 1

        # so here we can modify left and right

        # so the starting left would be something like left = 0 + rotation 

        # and right would be something like right = 0 + rotation

        # but this is what the while loop see

        # when we compare 


        # actually wait, we do not know the rotation number (how many times it rotated)
        # because if we know, then we know exactly which element is the smallest, (0 + rotation)

        # so what can we do in this case

        # can we just to binary search on the given input, what will happen

        # lets think from the first example
        # [3,4,5,6,1,2]

        # what will happen if we do binary search on this, and what things are we actually searching, what is the things we are comparing

        # left = 3, right = 2, mid 6

        # mid > left, so right smallest would not be on the left side, must be on the right side
        # is this true.
        # a counter example would be something like, [4,5,6,7]
        # so this is not true,

        # maybe we need to compare both left and right
        # if mid > left and mid > right, then right side

        # if mid > left and < right, left side

        # if mid < left and < right, left side

        # if mid < left and > right, is this possible?


        # got this hint: Try this: just compare nums[mid] against nums[right]. That single comparison is enough to decide which half to go to. Think about why, and try coding it.

        # so we only need to compare mid to the right because, this is a sorted array,

        # so if mid > right, right side
        # if mid < right, left side

        # and there is not mid == right, as nums are unique

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
                # i include mid because i believe mid could be the solution right
        
        return nums[left]