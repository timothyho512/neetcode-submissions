class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        ans = 0
        freq = defaultdict(int)
        maxFreq = 0
        current = 0

        while left < len(s) and right < len(s):

            freq[s[right]] += 1
            maxFreq = max(maxFreq, freq[s[right]])
            current = (right - left + 1) - maxFreq

            while current > k:
                freq[s[left]] -= 1
                left += 1
                current = (right - left + 1) - maxFreq


            ans = max(ans, right - left + 1)
            right += 1
            
        
        return ans