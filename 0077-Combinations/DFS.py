class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        current = []
        def bfs(start: int):
            if len(current) == k:
                result.append(current[:])
                return
            for j in range(start, n+1):
                current.append(j)
                bfs(j+1)
                current.pop()
        bfs(1)
        return result
