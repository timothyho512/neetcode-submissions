class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # so because things are sorted, we can definitely do binary search here

        # but the problem is how do we do it on the matrix

        # one cheat is loop through the whole matrix and build an array but then this would be O(MN) which is definitely
        # something we want to avoid (otherwise we dont need to use binarys earch anyway)

        # for me right now i think the most logical thing to do 
        # is to take the last digit of each row, and do binary search in that
        # so we found out which row and then do binary search on that row

        n = len(matrix[0]) - 1
        arr = []
        for i in range(len(matrix)):
            arr.append(matrix[i][n])
        
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2

            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                left = mid + 1
            elif arr[mid] > target:
                right = mid - 1
        #now left should the index of that row
        if left >= len(matrix):
            return False
        arr = matrix[left]

        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2

            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                left = mid + 1
            elif arr[mid] > target:
                right = mid - 1
        return False