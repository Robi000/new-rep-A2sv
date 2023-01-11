class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        i = 0
        count = 0
        players = list(range(n))
        remaning = n

        while remaning > 1:
            if players[i % n] != -1:
                count += 1

            if count == k:
                count = 0
                players[i % n] = -1
                remaning -= 1
            i += 1

        return (sum(players)+n)
