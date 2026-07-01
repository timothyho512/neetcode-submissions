class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # so here, very similar to the last question

        # but the only difference here is we are not finding the minimum.

        # we are actually finding the exact target value

        # so what does this tell us about the question

        # last question we compare mid to right because we are trying to find the minmum

        # so i am think we need to have two conditions

        # we need to keep the mid and right comparison

        # to see if right side has the minimum or the left side has the minimum

        # and also check if mid is == target

        # or it is < or > than target

        # if right side has the minimum and mid is < target

        # actually then we cant tell anything, it can go both ways

        # one very straight forward solution i can think of

        # is do the binary search just like the last question then we know where exactly the minimum is
        # so we know the rotation amount and the starting index

        # so we can do binary search using this information. so it will be O(2logn) and therefore O(logn)
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid        # mid is a candidate for minimum
            else:
                left = mid + 1     # mid is definitely not the minimum

        # now left is the starting index of a sorted array

        # so left = left
        # right = len(nums) + left

        # this is what the while loop see

        # and to find the index, we need to do some maths
        # real_index = sth % len(nums)

        left = left
        right = left + len(nums)

        while left <= right:
            mid = (left + right) // 2
            real_index = mid % len(nums)
            if nums[real_index] == target:
                return real_index
            elif nums[real_index] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1