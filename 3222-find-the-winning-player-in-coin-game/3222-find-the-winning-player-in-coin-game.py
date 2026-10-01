class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        turn = 1
        while x > 0 and y >= 4:
            x -= 1
            y -= 4
            turn ^= 1
        return "Alice" if not turn else "Bob"