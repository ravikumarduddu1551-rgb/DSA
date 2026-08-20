class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        i, j = 0, 0
        res = -1
        counter = defaultdict(int)
        for j in range(len(s)):
            counter[s[j]] += 1
            while counter[s[j]] > 1:
                counter[s[i]] -= 1
                i += 1
            res = max(res, j-i+1)
        return res
        
            