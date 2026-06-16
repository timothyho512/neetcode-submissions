class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        big_hash = dict()
        
        for s in strs:
            s_arr = [0] * 26
            for i in range(len(s)):
                n = ord(s[i]) - ord('a')
                s_arr[n] += 1
            key = tuple(s_arr)
            if key in big_hash:
                big_hash[key].append(s)
            else:
                big_hash[key] = [s]
        
        for key in big_hash:
            ans.append(big_hash[key])
        return ans
        # return list(big_hash.values())
        


