class Solution:
    def smallestNumber(self, pattern: str) -> str:
        ans = [str(i) for i in range(1,len(pattern)+2)]
        i = 0
        while i < len(pattern):
            if pattern[i] == 'D':
                j = i
                while j < len(pattern) and pattern[j] == 'D':
                    j += 1
                ans[i:j+1] = ans[i:j+1][::-1]
                i = j
            else:
                i += 1
        return "".join(ans)