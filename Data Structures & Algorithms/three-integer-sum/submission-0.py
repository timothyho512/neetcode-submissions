class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        h = defaultdict(list)

        count = defaultdict(list)

        ans = []

        for i in range(len(nums)):
            count[nums[i]].append(i)
            for j in range(i+1, len(nums)):
                total = nums[i] + nums[j]

                num = -total
                h[num].append((i, j))


        for key in h:
            if key in count:
                for j in h[key]:

                    f, s = j
                    for i in count[key]:
                        if i != f and i != s:
                            triplet = sorted([nums[f], nums[s], key])

                            if triplet not in ans:
                                ans.append(triplet)

        return ans
