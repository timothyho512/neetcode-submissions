import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # now as i know this question is related to binary search

        # how is this question related to binary search

        # because one important thing is for binary search to happen, the arr has to be sorted right

        # here it is not

        # so i remember we are not doing the binary search on the array, i think we are doing the binary search on something elese

        # which is like an integer or something

        # i think either on the solution itself or h maybe?

        # so something like can we do in  9 // 2 () works
        # yes then do 4 //2 and then do 2

        # then 1 no

        # so we know 2 is the answer

        # but here we are doing like O(nlogh) where n is the length of the piles which is not good no?

        # but we could argue logh is small?

        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2

            total = 0

            for i in range(len(piles)):
                total += math.ceil(piles[i] / mid)
            if total > h:
                left = mid + 1
            else:
                right = mid
        return left
