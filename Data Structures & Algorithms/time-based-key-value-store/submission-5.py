class TimeMap:

    # so definitely there is a hashmap and the key is the String key
    # and thinking we can do something like an array of timestampt
    # because it is strickly increasing so 1,2,3,4,5,6 no missing in between or 1,3,2 sth like that
    # then we can have an array that correspond to this to store the String value

    # so set we add values to the array

    # and get, we need to use binary search to find the largets timestamp_prev and then use the array to output

    def __init__(self):
        # do i have a struct or just a tuple inside the hashmap
        self.hashmap = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            # lets say first array is the timestamp and second is for the value
            self.hashmap[key] = [[], []]
        self.hashmap[key][1].append(value)
        self.hashmap[key][0].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""
        arr = self.hashmap[key][0]

        left = 0
        right = len(arr) - 1

        while left < right:
            mid = (left + right + 1) // 2

 
            if arr[mid] <= timestamp:
                left = mid
            else:
                right = mid - 1
        # left should be the index now
        if arr[left] > timestamp:
            return ""
        return self.hashmap[key][1][left]
