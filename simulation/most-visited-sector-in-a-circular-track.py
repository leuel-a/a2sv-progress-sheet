class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        m = len(rounds)
        sectors = [0 for _ in range(n)]

        for i in range(1, m):
            k = rounds[i - 1]
            end = rounds[i]

            while k != end:
                sectors[k - 1] += 1
                k = k + 1 if k + 1 <= n else 1
        sectors[rounds[-1] - 1] += 1

        result = []
        max_freq = max(sectors)
        for idx, val in enumerate(sectors):
            if val == max_freq:
                result.append(idx + 1)
        return result