class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # thoughts and thinking process
        # i could have a hashmap storing which character appears how many times, 
        # but then if i need to quick access, then the appearance time has to be the key
        # which is weird

        # or i could sort the thing arr out first, then we could just loop through the arr
        # and always store the top k frequent elements, but then this would mean the time complexity would increase due to the sorting

        # if we dont sort, we would need a hashmap that have the integer as key
        # and the number of appearance as value
        # then we loop through the arr, and each time we need to check if the number
        # is in the answer array already, if not, need to compare k times for each of the number in the k array and find their appearance number and compare

        buckets = [[] for _ in range(len(nums) + 1)]
        n_hash = defaultdict(int)
        ans = []

            
        for n in nums:
            n_hash[n] += 1
            
        for num, freq in n_hash.items():
            buckets[freq].append(num)

        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                ans.append(num)

                if len(ans) == k:
                    return ans
        