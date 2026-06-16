class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> bigHash;

        for (string s : strs) {
            vector<int> count(26, 0);

            for (char c : s) {
                count[c - 'a']++;
            }

            string key = "";
            for (int n : count) {
                key += to_string(n) + "#";
            }

            bigHash[key].push_back(s);
        }

        vector<vector<string>> ans;
        for (auto& pair : bigHash) {
            ans.push_back(pair.second);
        }

        return ans;
    }
};