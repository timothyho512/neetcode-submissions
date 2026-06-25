class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        seen = set()
        ans = 0

        while left < len(s) and right < len(s):
            if s[right] in seen:
                seen.remove(s[left])
                left += 1
            
            else:
                ans = max(ans, right - left + 1)
                seen.add(s[right])
                right += 1
        
        
        return ans