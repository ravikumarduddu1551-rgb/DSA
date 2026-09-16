class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        seen = set()
        for perm in permutations(digits, 3):
            if perm[0] == 0:
                continue
            num = perm[0] * 100 + perm[1] * 10 + perm[2]
            if num % 2 == 0:
                seen.add(num)
        return len(seen)
        