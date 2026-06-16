class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) {
            return false;
        }

        unordered_map<char, int> s_hash;
        unordered_map<char, int> t_hash;

        for (int i = 0; i < s.length(); i++) {
            s_hash[s[i]]++;
            t_hash[t[i]]++;
        }

        return s_hash == t_hash;
    }
};