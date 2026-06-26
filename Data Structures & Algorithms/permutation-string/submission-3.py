class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # so sliding window

        # what I am thinking right now is that we need to have a hashmap
        # to remember the the freq each character has appeared in s1
        # the reason why we cannot use set is because we need to know the exact freq of appearance

        # and then we loop through s2, if the left character is not in s1, then left += 1
        # if it is inside s1, then we move right +=1
        # same logic applies, and if one of the character freq is higher that in s1
        # then we need to start moving left += 1 again

        # or because this is lowercase only, meaning there is only 26
        # so could we use an array here, where a is in index 0 storing the appearance freq
        # it would be easier? or it is just the same

        s1_hash = defaultdict(int)
        s2_hash = defaultdict(int)
        if len(s2) < len(s1):
            return False

        for i in range(len(s1)):
            s1_hash[s1[i]] += 1
            s2_hash[s2[i]] += 1
        
        if s2_hash == s1_hash:
            return True
        
        for i in range(len(s1), len(s2)):
            s2_hash[s2[i]] += 1
            s2_hash[s2[i-len(s1)]] -= 1
            if s2_hash[s2[i-len(s1)]] == 0:
                del s2_hash[s2[i-len(s1)]]

            if s2_hash == s1_hash:
                return True
            
        
        return False