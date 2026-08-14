class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        freq = defaultdict(int)
        i = 0
        l = 0
        for j in range(len(s)):
            freq[s[j]] += 1
            while freq[s[j]] > 2:
                freq[s[i]] -= 1
                i += 1
            l = max(l, j - i + 1)
        return l